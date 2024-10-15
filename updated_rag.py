import glob
import logging
import os
from contextlib import asynccontextmanager
from multiprocessing import Pool
from typing import List

import ollama
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.chains.qa_with_sources.base import BaseQAWithSourcesChain
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import LlamaCpp
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import MarkdownHeaderTextSplitter
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from tqdm import tqdm

load_dotenv()

# Load environment variables
source_directory = os.environ.get("SOURCE_DIRECTORY")
stride = os.environ.get("STRIDE")
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
chunk_size = 256
chunk_overlap = 50
model_type = os.environ.get("MODEL_TYPE")
model_path = os.environ.get("MODEL_PATH")
model_n_ctx = os.environ.get("MODEL_N_CTX")
model_n_batch = int(os.environ.get("MODEL_N_BATCH", 8))
target_source_chunks = int(os.environ.get("TARGET_SOURCE_CHUNKS", 4))
model: BaseQAWithSourcesChain


def load_markdown(file_path: str):
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ("####", "Header 4"),
        ("#####", "Header 5"),
        ("######", "Header 6"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    md_header_splits = markdown_splitter.split_text(content)
    for md in md_header_splits:
        md.metadata["source"] = file_path
    return md_header_splits


def load_images(file_path: str):
    absolute_path = os.path.abspath(file_path)
    res = ollama.chat(
        model="llava",
        messages=[
            {
                "role": "user",
                "content": "describe this image and make sure to include anything notable about it (include text you see in the image):",
                "images": [absolute_path],
            }
        ],
    )
    content = res["message"]["content"]
    print("Image Content", absolute_path)
    return [Document(page_content=content, metadata={"source": file_path})]


def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    pages = []
    for page in loader.lazy_load():
        print("PDF content", page)
        pages.append(page)
    return pages


MAPPINGS = {
    ".md": load_markdown,
    # ".jpg":load_images,
    # ".jpeg":load_images,
    # ".png":load_images,
    # ".pdf":load_pdf,
}


def load_single_document(file_path: str) -> List[Document]:
    ext = "." + file_path.rsplit(".", 1)[-1]
    if ext in MAPPINGS:
        loader_class = MAPPINGS[ext]
        return loader_class(file_path)
    raise ValueError(f"Unsupported file extension '{ext}'")


def load_documents(source_dir: str, ignored_files: List[str] = []) -> List[Document]:
    """
    Loads all documents from the source documents directory, ignoring specified files
    """
    results = []
    image_files = (
        glob.glob(os.path.join(f"{source_dir}/static", "**/*.jpg"), recursive=True)
        + glob.glob(os.path.join(f"{source_dir}/static", "**/*.jpeg"), recursive=True)
        + glob.glob(os.path.join(f"{source_dir}/static", "**/*.png"), recursive=True)
    )
    markdown_files = glob.glob(
        os.path.join(source_dir, "**/*.[mM][dD]"), recursive=True
    )
    pdf_files = glob.glob(os.path.join(source_dir, "**/*.[pP][dD][fF]"), recursive=True)
    all_files = markdown_files
    with Pool(processes=os.cpu_count()) as pool:
        with tqdm(total=len(all_files), desc="Loading documents", ncols=80) as pbar:
            for j, docs in enumerate(
                pool.imap_unordered(load_single_document, all_files)
            ):
                results.extend(docs)
                pbar.update(1)
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
    return documents


@asynccontextmanager
async def lifespan(_app: FastAPI):
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)  # noqa
    try:
        os.listdir("updated_index")

    except FileNotFoundError:
        print("Creating new vectorstore")
        texts = process_documents()
        print(f"Creating embeddings. May take some minutes...")
        db = FAISS.from_documents(texts, embeddings)
        db.save_local("updated_index")
        print(f"Ingestion complete! You can now query your visual documents")

    # loading the vectorstore
    db = FAISS.load_local(
        "updated_index", embeddings, allow_dangerous_deserialization=True
    )
    retriever = db.as_retriever(
        search_type="similarity", search_kwargs={"k": target_source_chunks}
    )
    prompt_template = """
        <<SYS>>
    You are a helpful assistant working in Example Company you know everything about the company , who can only provide answers based on the given summaries.
    If the answer is not in the summaries,strictly respond with **I don't know**.
    Remember, The user would be asking questions as an employee to you, Be Friendly
    This is the holiday calender for the employee:
    ## The Example Company Employee Leave Calendar for enquiry of leaves in 2024

January
- New Year's Day: On Monday, January 1, 2024, employees will celebrate the arrival of the new year. This marks the beginning of the calendar year and provides a day for rest and renewal.
- Martin Luther King Jr. Day: Observed on Monday, January 15, 2024, this day commemorates the life and achievements of Dr. Martin Luther King Jr., a key figure in the civil rights movement.

February
- Presidents' Day (Washington's Birthday): On Monday, February 19, 2024, we honor the contributions of all U.S. presidents, with a special focus on the first president, George Washington.

May
- Memorial Day: Monday, May 27, 2024, is a day of remembrance for those who have died in military service to the United States. It also marks the unofficial beginning of summer.

June
- Juneteenth National Independence Day: On Wednesday, June 19, 2024, we celebrate the end of slavery in the United States, commemorating the day in 1865 when enslaved people in Texas were informed of their freedom.

July
- Independence Day: On Thursday, July 4, 2024, we celebrate the Declaration of Independence and the birth of the United States.

September
- Labor Day: On Monday, September 2, 2024, we honor the American labor movement and the contributions of laborers to the development of the country.

October
- Columbus Day: Observed on Monday, October 14, 2024, this holiday commemorates Christopher Columbus's arrival in the Americas, although it is recognized as Indigenous Peoples' Day in some states.

November
- Veterans Day: On Monday, November 11, 2024, we honor military veterans who have served in the U.S. Armed Forces.
- Thanksgiving Day: On Thursday, November 28, 2024, we gather with family and friends to give thanks for the harvest and blessings of the past year.
- Day After Thanksgiving: On Friday, November 29, 2024, this optional leave day is often taken to extend the Thanksgiving holiday.

December
- Christmas Day: On Wednesday, December 25, 2024, we celebrate Christmas, a holiday observed by many to commemorate the birth of Jesus Christ.

    <</SYS>>
    {summaries}\n\n
    [INST]
    User:{question}
    [/INST]\n
    Assistant:
    """
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["summaries", "question"]
    )
    chain_type_kwargs = {"prompt": PROMPT}
    llm = LlamaCpp(
        model_path=model_path,
        n_gpu_layers=400,
        n_batch=512,
        f16_kv=True,
        callback_manager=None,
        n_ctx=5000,
        temperature=0.0,
        use_mlock=True,
    )
    global model
    model = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True,
        chain_type_kwargs=chain_type_kwargs,
    )
    yield
    # Clean up the ML models and release the resources


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="handbook"), name="static")
origins = [
    "http://localhost:5173/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatInput(BaseModel):
    input: str


@app.get("/chat")
async def chat(question: str):
    global model
    logging.debug(f"QUESTION {question}")
    response = model.invoke({"question": question})
    urls = []
    images = []
    logging.debug(f"RESPONSE: {response}")
    for doc in response.get("source_documents", []):
        if filename := doc.metadata.get("source"):
            urls.append(filename.replace("handbook", ""))
    return {"Answer": response.get("answer"), "Images": images, "Urls": urls}
    # response.get("source_documents")


@app.get("/chat/models")
async def models():
    return {"models": ["llava-v1.6-vicuna-7b"]}


if __name__ == "__main__":
    pass
