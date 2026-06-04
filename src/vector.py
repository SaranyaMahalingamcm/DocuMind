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
    collection = client.create_collection("documind")
    for i, chunk in enumerate(chunks):
        embedding=embedder.encode(chunk).tolist()
        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[chunk]
        )
    return collection



 # # client = chromadb.HttpClient()
    # import os

    # # Check which environment we are in
    # environment = os.environ.get("ENVIRONMENT", "development")
    # # os.environ.get reads environment variables
    # # "development" is default if not set

    # if environment == "development":
    #     # local development — use memory
    #     client = chromadb.Client()

    # elif environment == "production":
    #     # deployed — use persistent storage
    #     client = chromadb.PersistentClient(
    #         path="./chroma_store"
    #     )