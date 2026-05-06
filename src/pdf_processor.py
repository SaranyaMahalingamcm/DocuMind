# # pdf_processor.py
# # Responsibility: Read a PDF and split it into chunks

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


def text_chunk(text, size=100, overlap=50):
    chunks = []
    start=0
    while len(text)>start:
        end = start+size
        chuck_text=text[start:end]
        chuck_text.strip()
        if chuck_text !="":
            chunks.append(chuck_text)
        start=end-overlap
    return chunks

def metadata(uploaded_file):
    reader= PdfReader(uploaded_file)
    page_count=len(reader.pages)
    meta=reader.metadata or {}      
    title=meta.get("/Title","unknown")
    author=meta.get("/Author","unknown")
    return{
        'pages': page_count,
        'title': title,
        'author':author
    }