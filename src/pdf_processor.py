from pypdf import PdfReader

# function 1 - to extract the texts from the pdf

def text_extract(uploaded_file):
    reader = PdfReader(uploaded_file) # reader object
    pages = []
    for page in reader.pages:
        extracted_texts = page.extract_text()
        if extracted_texts != '':
            pages.append(extracted_texts)
    return "\n".join(pages)

# Function 2- to extract chunk
def chunk_text(text, chunk_size=500,overlap=50):
    chunks=[]
    start = 0
    while len(text)>start:
        end=start+chunk_size
        chunk=text[start:end]
        chunk=chunk.strip()
        if chunk != "":
            chunks.append(chunk)
        start= end-overlap
    return chunks

#function 3- to extract metadata

def get_metadata(uploaded_file):
    reader=PdfReader(uploaded_file)
    meta=reader.metadata or {}
    title= meta.get("/Title","Unknown")
    author= meta.get("/Author","Unknown")
    return {
    "pages": len(reader.pages),
    "title": title,
    "author": author
    }


