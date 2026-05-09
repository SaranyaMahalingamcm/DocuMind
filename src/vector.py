import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

@st.cache_resource

def load_embedder():
    model=SentenceTransformer("all-MiniLM-L6-v2")
    return model

client = chromadb.Client() # in memory database

def build_vector_store(chunks):

    # Step 1 - load embedding model
    embedder = load_embedder()
    # load_embedder() is our Function 1
    # returns the SentenceTransformer model
    # ready to convert text to numbers

    # Step 2 - create empty database
    client = chromadb.Client()
    # creates in-memory ChromaDB database
    # like opening empty Excel file

    # Step 3 - create collection inside database
    collection = client.create_collection("documind")
    # creates named section in database
    # like creating a sheet in Excel
    # "documind" is our chosen name

    # Step 4 - loop through each chunk with index
    for i, chunk in enumerate(chunks):
        # i     = 0, 1, 2, 3... (position number)
        # chunk = actual text of this chunk

        # Step 5 - convert chunk text to embedding
        embedding = embedder.encode(chunk).tolist()
        # encode() converts text to 384 numbers
        # tolist() converts to Python list for ChromaDB

        # Step 6 - store in collection
        collection.add(
            ids=[str(i)],        # "0", "1", "2"...
            embeddings=[embedding], # [[0.12, -0.45...]]
            documents=[chunk]    # ["chunk text here"]
        )
        # adds one row to our collection
        # id + embedding + original text stored together

    # Step 7 - return collection
    return collection
    # returns the filled collection
    # app.py passes this to search_chunks() later

