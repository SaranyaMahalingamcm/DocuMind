import streamlit as st
import google.generativeai as genai

@st.cache_resource

def load_llm():
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-2.5-flash")
    return model