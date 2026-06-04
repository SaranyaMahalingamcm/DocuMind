import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

#load embedder
@st.cache_resource
def load_embedder():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model

def build_vector_store(chunks):
    embedder = load_embedder()
    client = chromadb.Client()
    try:
        client.delete_collection("documind")
    except:
        pass  # does not exist yet — that is fine
    
    # Create fresh collection
    collection = client.create_collection("documind")
    for i, chunk in enumerate(chunks):
        embedding=embedder.encode(chunk).tolist()
        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[chunk]
        )
    return collection

def search_chunks(userquestion,collection):
    embedder = load_embedder()
    userquestion_embedding = embedder.encode(userquestion).tolist()
    query_result= collection.query(
        query_embeddings=[userquestion_embedding],
        n_results = 3
    )
    end_return = query_result["documents"][0]
    return end_return
