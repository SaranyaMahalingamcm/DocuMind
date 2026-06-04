import src.pdf_processor as pdf
import src.vector as vec
import src.llm as llm
import streamlit as st

st.set_page_config(
    page_title="Documind",
    layout="centered"
    )

st.title("Documind")
uploaded_file= st.file_uploader("Upload pdf",type=["pdf"])

if uploaded_file is not None:

    # Check if NEW file uploaded
    if "current_file" not in st.session_state or \
        st.session_state["current_file"] != uploaded_file.name:
        st.write(f"Processing new file: {uploaded_file.name}")
        # New file detected — process it
        with st.spinner("Processing PDF..."):
            text = pdf.text_extract(uploaded_file)
            chunks = pdf.chunk_text(text)
            collection = vec.build_vector_store(chunks)
            st.session_state["collection"] = collection
            st.session_state["current_file"] = uploaded_file.name
        st.success("✅ PDF Processed!")

    question = st.text_input("Ask question about the uploaded file")

    if question:
        with st.spinner("Thinking..."):
            collection = st.session_state["collection"]
            chunks = vec.search_chunks(question, collection)
            answer = llm.generate_answerforuser(question, chunks)
        st.write("### Answer")
        st.write(answer)