# Project Overview

This project implements two vector database retrieval systems for efficient document search.

## Dependencies

The project relies on the following files and external resources:

* **faiss_rag.py**: Script for the Faiss vector database system.
* **chroma_rag.py**: Script for the Chroma vector database system.
* **Model**: Download the model from [https://huggingface.co/cjpais/llava-v1.6-vicuna-7b-gguf/resolve/main/llava-v1.6-vicuna-7b.Q3_K_M.gguf](https://huggingface.co/cjpais/llava-v1.6-vicuna-7b-gguf/resolve/main/llava-v1.6-vicuna-7b.Q3_K_M.gguf).
    * Save it under: `models/llava-v1.6-vicuna-7b.Q3_K_M.gguf`
* **requirements.txt**: File containing project dependencies. Use this to create a virtual environment and install the required packages.

## Vector Databases

* **Faiss**: Stores vectors in a Faiss index for efficient retrieval.
    * Index location: `updated_index` directory.
* **Chroma**: Utilizes a Chroma-based approach for faster search performance.
    * Index location: `chroma_index` directory.

## Running the Project

The server automatically generates the vector databases (`updated_index` and `chroma_index`) if they are not present. These databases are built from document information found in the `.env` file.

**Chroma Database Server:**

```bash
uvicorn chroma_rag:app --host 0.0.0.0 --port 8000 --reload
```


**Faiss Database Server:**
```bash
uvicorn faiss_rag:app --host 0.0.0.0 --port 8000 --reload
```

PS: The prompt template for faiss_rag is inside the python file itself, while chroma_rag is from the data/prompt_templates directory

PS: check tailscale!, 
