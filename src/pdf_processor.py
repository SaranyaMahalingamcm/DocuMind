from pypdf import PdfReader

# function 1 - to extract the texts from the pdf

def extract_text(file_uploaded):
    reader = PdfReader(file_uploaded)
    pages= []
    for page in reader.pages:
        text=page.extract_text()
        if text != '':
            pages.append(text)
        
    return "\n".join(pages)

#function 2

def chunk_text(text, chunk_size=500,overlap=50):
    chunks=[]
    start=0
    while len(text)>start:
        end=start+chunk_size
        chunk=text[start:end]
        if chunk != '':
            chunks.append(chunk)
        start=end-overlap
    return chunks

#function 3
def get_metadata(file_uploaded):
    file = PdfReader(file_uploaded)
    page_count = len(file.pages)
    meta = file.metadata or {}
    return{
        'pages':page_count,
        'title':meta.get("/Title","unknown"),
        'author':meta.get("/Author","unknown")
    }
