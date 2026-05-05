# pdf_processor.py
# Responsibility: Read a PDF and split it into chunks

from pypdf import PdfReader


def extract_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    page_text=[] #create an empty list

    for page in reader.pages(): # loop the variable through each pages extracted by the reader
        text=page.extract_text() # extract all the texts in the page using the inbuild function and save in the variable text

        if text != "":
            page_text.append(text) # If the text is not empty, append the values in text to page_text list   
    all_texts="\n".join(page_text)

    return all_texts


def chunk_texts(texts, chunk_size=500, overlap=50):
    chunk_text=[]
    starting=0
    text_len=len(texts)
    ending=len(texts)
   # for text in starting<= text_len:



def get_pdf_metadata(uploaded_file):
    reader = PdfReader(uploaded_file)
    meta = reader.metadata or {}
    return {
        "pages": len(reader.pages),
        "title": meta.get("/Title", "Unknown"),
        "author": meta.get("/Author", "Unknown")
    }