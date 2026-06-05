# DocuMind 🧠
> Chat with your PDFs using AI

Upload any PDF and ask questions in plain English.
Powered by RAG, Google Gemini, and ChromaDB.

## 🚀 Live Demo
[Click here to try DocuMind](https://pdfreadoc.streamlit.app/)

## 🎯 How It Works
PDF Upload → Extract Text → Chunk → Embed → Store in ChromaDB
User Question → Embed → Search → Send to Gemini → Answer

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **PDF Processing:** pypdf
- **Embeddings:** sentence-transformers
- **Vector DB:** ChromaDB
- **LLM:** Google Gemini 2.5 Flash

## ⚙️ Setup
1. Clone the repo
2. Install dependencies:
pip install -r requirements.txt
3. Add your Google API key to `.streamlit/secrets.toml`:
GOOGLE_API_KEY = "your-key-here"
4. Run:
streamlit run app.py

## 🗺️ Roadmap
- [ ] Multi-session support
- [ ] Qdrant vector database
- [ ] HuggingFace models
- [ ] Ollama for local deployment
- [ ] MCP integration