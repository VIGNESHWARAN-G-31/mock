# Agentic RAG using Hugging Face and FAISS (Free)

## Project Structure
```
agentic_rag/
├── main.py
├── retriever.py
├── embeddings.py
├── agent.py
├── utils.py
├── document_store/
│   └── docs.json
├── prompts/
│   ├── planner.txt
│   ├── retriever.txt
│   └── answer.txt
├── doc_texts.json
├── faiss.index
├── requirements.txt
└── README.md
```

## Setup
1. **Create and activate a virtual environment**
   - Run `setup_env.bat` (Windows) or manually:
     ```
     python -m venv venv
     venv\Scripts\activate
     pip install -r requirements.txt
     ```
2. **Build the FAISS index**
   ```
   python embeddings.py
   ```
3. **Run the main agent**
   ```
   python main.py
   ```

## Usage
- When prompted, enter your question (e.g., "What is the leave policy for remote employees?").
- The agent will plan, retrieve relevant documents, and answer using only the provided context.

## Notes
- LLMs used: `falcon-rw-1b` (for planning), `mistralai/Mistral-7B-Instruct-v0.2` (for answering)
- Hugging Face free tier supports these models.
- Add more documents to `document_store/docs.json` and rerun `embeddings.py` to update the index. 
