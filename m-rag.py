import glob
import os
from contextlib import asynccontextmanager
from multiprocessing import Pool
from typing import List

import imageio
import ollama
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    CSVLoader,
    EverNoteLoader,
    PyMuPDFLoader,
    TextLoader,
    UnstructuredEmailLoader,
    UnstructuredEPubLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    UnstructuredODTLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
)
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import LlamaCpp
from langchain_community.vectorstores import FAISS
from pydantic import BaseModel
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from tqdm import tqdm

load_dotenv()

#  Load environment variables
source_directory = os.environ.get('SOURCE_DIRECTORY')
stride = os.environ.get('STRIDE')
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME')
chunk_size = 256
chunk_overlap = 50
model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
model_n_batch = int(os.environ.get('MODEL_N_BATCH', 8))
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS', 4))


# Replace with the actual path to your FFmpeg executable


def img_parse(img_path):
    res = ollama.chat(
        model="llava",
        messages=[
            {
                'role': 'user',
                'content': 'describe this image and make sure to include anything notable about it (include text you see in the image):',
                'images': [img_path]
            }
        ]
    )

    with open(source_directory + "/" + os.path.basename(img_path) + ".txt", "a") as write_file:
        write_file.write("---" * 10 + "\n\n")
        write_file.write(os.path.basename(img_path) + "\n\n")
        write_file.write(res['message']['content'])
        write_file.flush()
    print("Proceeding " + img_path)


# parse the video with llava into txt if source_documents is empty
def video_parse(video_path):
    reader = imageio.get_reader(video_path)
    meta = reader.get_meta_data()
    try:
        total_frames = meta["n_frames"]  # Access frame count from metadata (if available)
    except KeyError:
        print("Frame count not found in metadata. Counting frames manually...")
        total_frames = 0
        for _ in reader:
            total_frames += 1

    print(f"Number of frames: {total_frames}")

    for i in tqdm(range(total_frames)):

        frame = reader.get_next_data()

        if i % int(stride) == 0:
            # Save the image to a file
            imageio.imsave('temp.png', frame)
            res = ollama.chat(
                model="llava",
                messages=[
                    {
                        'role': 'user',
                        'content': 'describe this image and make sure to include anything notable about it (include text you see in the image):',
                        'images': ['./temp.png']
                    }
                ]
            )

            with open(source_directory + "/" + os.path.basename(video_path) + ".txt", "a") as write_file:
                write_file.write("---" * 10 + "\n\n")
                write_file.write(os.path.basename(video_path) + "(Frame:" + str(i) + ")" + "\n\n")
                write_file.write(res['message']['content'])
                write_file.flush()

    reader.close()
    print("Proceeding " + video_path)


# Custom document loaders
class MyElmLoader(UnstructuredEmailLoader):
    """Wrapper to fallback to text/plain when default does not work"""

    def load(self) -> List[Document]:
        """Wrapper adding fallback for elm without html"""
        try:
            try:
                doc = UnstructuredEmailLoader.load(self)
            except ValueError as e:
                if 'text/html content not found in email' in str(e):
                    # Try plain text
                    self.unstructured_kwargs["content_source"] = "text/plain"
                    doc = UnstructuredEmailLoader.load(self)
                else:
                    raise
        except Exception as e:
            # Add file_path to exception message
            raise type(e)(f"{self.file_path}: {e}") from e

        return doc


# Custom video loader
class VideoLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self) -> List[Document]:
        try:
            video_parse(self.file_path)
            loader = TextLoader(source_directory + "/" + os.path.basename(self.file_path) + ".txt")
            doc = loader.load()
        except Exception as e:
            # Add file_path to exception message
            raise type(e)(f"{self.file_path}: {e}") from e
        return doc


class ImgLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self) -> List[Document]:
        try:
            img_parse(self.file_path)
            loader = TextLoader(source_directory + "/" + os.path.basename(self.file_path) + ".txt")
            doc = loader.load()
        except Exception as e:
            # Add file_path to exception message
            raise type(e)(f"{self.file_path}: {e}") from e
        return doc


# Map file extensions to document loaders and their arguments
LOADER_MAPPING = {
    ".csv": (CSVLoader, {}),
    ".doc": (UnstructuredWordDocumentLoader, {}),
    ".docx": (UnstructuredWordDocumentLoader, {}),
    ".enex": (EverNoteLoader, {}),
    ".eml": (MyElmLoader, {}),
    ".epub": (UnstructuredEPubLoader, {}),
    ".html": (UnstructuredHTMLLoader, {}),
    ".md": (UnstructuredMarkdownLoader, {"mode": "elements"}),  # to chunkify reading
    ".odt": (UnstructuredODTLoader, {}),
    ".pdf": (PyMuPDFLoader, {}),
    ".ppt": (UnstructuredPowerPointLoader, {}),
    ".pptx": (UnstructuredPowerPointLoader, {}),
    ".txt": (TextLoader, {"encoding": "utf8"}),
    ".mp4": (VideoLoader, {}),
    ".jpg": (ImgLoader, {}),
    ".jpeg": (ImgLoader, {}),
    ".png": (ImgLoader, {}),
    # Add more mappings for other file extensions and loaders as needed
}


def load_single_document(file_path: str) -> List[Document]:
    ext = "." + file_path.rsplit(".", 1)[-1]
    if ext in LOADER_MAPPING:
        loader_class, loader_args = LOADER_MAPPING[ext]
        loader = loader_class(file_path, **loader_args)

        return loader.load()

    raise ValueError(f"Unsupported file extension '{ext}'")


def load_documents(source_dir: str, ignored_files: List[str] = []) -> List[Document]:
    """
    Loads all documents from the source documents directory, ignoring specified files
    """
    all_files = []
    for ext in LOADER_MAPPING:
        all_files.extend(
            glob.glob(os.path.join(source_dir, f"**/*{ext}"), recursive=True)
        )
    filtered_files = [file_path for file_path in all_files if file_path not in ignored_files]
    with Pool(processes=os.cpu_count()) as pool:
        results = []
        with tqdm(total=len(filtered_files), desc='Loading new documents', ncols=80) as pbar:
            for j, docs in enumerate(pool.imap_unordered(load_single_document, filtered_files)):
                results.extend(docs)
                pbar.update()

    return results


def process_documents(ignored_files: List[str] = []) -> List[Document]:
    """
    Load documents and split in chunks
    """
    print(f"Loading documents from {source_directory}")
    documents = load_documents(source_directory, ignored_files)
    if not documents:
        print("No new documents to load")
        exit(0)
    print(f"Loaded {len(documents)} new documents from {source_directory}")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} chunks of text (max. {chunk_size} tokens each)")
    return texts


model = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    # embeddings = GPT4AllEmbeddings()
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    try:
        os.listdir("faiss_index")

    except FileNotFoundError:
        # Create and store locally vectorstore if folder not exit
        print("Creating new vectorstore")
        texts = process_documents()
        print(f"Creating embeddings. May take some minutes...")
        db = FAISS.from_documents(texts, embeddings)
        db.save_local("faiss_index")
        print(f"Ingestion complete! You can now query your visual documents")

    # loading the vectorstore
    db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": target_source_chunks})
    prompt_template = """
        <<SYS>>
    You are a helpful Assistant who is working at UST, who can only provide answers based on the given summaries.
    If the answer is not in the summaries,simply respond with **I don't know**.
    Remember, The user would be asking questions to you, Be Friendly
    <</SYS>>
    {summaries}\n\n
    [INST]
    User:{question}
    [/INST]\n
    Assistant:
    """
    PROMPT = PromptTemplate(template=prompt_template, input_variables=['summaries', 'question'])
    chain_type_kwargs = {"prompt": PROMPT}
    # Callbacks support token-wise streaming
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    match model_type:
        case "LlamaCpp":
            llm = LlamaCpp(model_path=model_path, n_gpu_layers=10, n_batch=512, f16_kv=True,
                           callback_manager=None,
                           n_ctx=4096, temperature=0.0,
                           use_mlock=True,
                           # Lower temperature
                           )
        case _default:
            raise Exception(
                f"Model type {model_type} is not supported. Please choose one of the following: LlamaCpp, GPT4All")
    model['func'] = RetrievalQAWithSourcesChain.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff",
                                                                return_source_documents=True,
                                                                chain_type_kwargs=chain_type_kwargs)
    yield
    # Clean up the ML models and release the resources


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="ust_data"), name="static")
origins = [
    "http://localhost:5173/",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatInput(BaseModel):
    input: str


@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}


@app.get("/chat")
async def chat(question: str):
    print(question)
    response = model['func'](question)
    urls = []
    images = []
    for doc in response.get("source_documents", []):
        if filename := doc.metadata.get("source"):
            if filename.endswith(".txt"):
                filename = filename.replace("ust_data/", "images/")
                images.append(filename.replace(".txt", ""))
            else:
                urls.append("www." + filename.split("/")[-1].replace("_", "/").replace(".md", ""))
    return {"Answer": response.get("answer"), "Images": images, "Urls": urls}
    # response.get("source_documents")


@app.get("/chat/models")
async def models():
    return {"models": ["llava-v1.6-vicuna-7b"]}


if __name__ == "__main__":
    pass
