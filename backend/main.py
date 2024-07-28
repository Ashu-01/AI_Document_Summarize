from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
import shutil
from transformers import pipeline
from summarizer import Summarizer,TransformerSummarizer
import fitz  # PyMuPDF
import docx

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from the specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Load the summarization pipeline
summarizer = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")

def read_file_content(file_path: str) -> str:
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == ".pdf":
        return read_pdf_content(file_path)
    elif file_extension.lower() == ".docx":
        return read_docx_content(file_path)
    elif file_extension.lower() == ".txt":
        return read_txt_content(file_path)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

def read_pdf_content(file_path: str) -> str:
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def read_docx_content(file_path: str) -> str:
    doc = docx.Document(file_path)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text

def read_txt_content(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

@app.post("/upload")
async def upload_file(files: List[UploadFile] = File(...)):
    file_paths = []
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_paths.append(file_path)
    return {"file_paths": file_paths}

class SummarizeRequest(BaseModel):
    file_path: str

@app.post("/summarize")
async def summarize_file(request: SummarizeRequest):
    file_path = request.file_path
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    content = read_file_content(file_path)
    


    # Set max_new_tokens to define the maximum number of new tokens to generate
    summary = ''.join(summarizer(content, min_length=70))
    return {"summary": summary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
