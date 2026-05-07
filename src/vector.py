import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

@st.cache_resource

def load_embedder():
    model=SentenceTransformer("all-MiniLM-L6-v2")
    return model

client = chromadb.Client() # in memory database
collection = client.create_collection("documind")