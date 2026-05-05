# pdf_processor.py
# Responsibility: Read a PDF and split it into chunks

from pypdf import PdfReader


def extract_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    full_text = "\n".join(
        page.extract_text() for page in reader.pages
        if page.extract_text()
    )
    return full_text


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunk = chunk.strip()
        if chunk:
            chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


def get_pdf_metadata(uploaded_file):
    reader = PdfReader(uploaded_file)
    meta = reader.metadata or {}
    return {
        "pages": len(reader.pages),
        "title": meta.get("/Title", "Unknown"),
        "author": meta.get("/Author", "Unknown")
    }