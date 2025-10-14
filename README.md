# Simple RAG System (Qdrant + Groq + Streamlit)

This repository is a minimal Retrieval-Augmented Generation (RAG) proof-of-concept using:
- Embeddings: `sentence-transformers/all-mpnet-base-v2`
- Vector store: Qdrant (local or cloud)
- LLM: Groq-hosted models (optional; app will still show retrieved docs without LLM)
- UI: Streamlit

## Quickstart

1. Start Qdrant:
   ```bash
   docker-compose up -d
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows (PowerShell)
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your Groq API key (if available):
   ```bash
   cp .env.example .env
   # Edit .env to set GROQ_API_KEY
   ```

4. Ingest sample documents:
   ```bash
   python ingest/ingest_data.py
   ```

5. Run the Streamlit app:
   ```bash
   streamlit run app/rag_app.py
   ```

## Files

- `ingest/ingest_data.py` — creates sample embeddings and uploads to Qdrant.
- `app/rag_app.py` — Streamlit app to query the vector DB and optionally call Groq LLM.
- `docker-compose.yml` — to run local Qdrant.
- `.env.example` — environment variables.
- `sample_docs/` — sample document(s).

## Notes

- If you don't provide a `GROQ_API_KEY`, the Streamlit app will still retrieve and display relevant documents; it will indicate Groq is not configured for generation.
- For production, switch to token-based chunking, batching, and a robust ingestion pipeline.
