import streamlit as st
import google.generativeai as genai

@st.cache_resource

def load_llm():
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-2.5-flash")
    return model

def build_prompt(userquestion,chunks):
    context = "\n\n".join(chunks)
    llm_prompt = f""" 
    Answer the question based strictly on the provided context.
    Context:
    {context}

    Question:
    {userquestion}

    If the answer is not in the context
    say: I could not find that in the document
    """
    return llm_prompt

def generate_answerforuser(userquestion,chunks):
    model = load_llm()
    prompt = build_prompt(userquestion,chunks)
    response= model.generate_content(prompt)
    return response.text