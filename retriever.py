from sentence_transformers import SentenceTransformer
import faiss, json, numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index('faiss.index')
with open('doc_texts.json') as f:
    texts = json.load(f)

def retrieve_relevant_docs(query, k=3):
    vec = model.encode([query])
    D, I = index.search(np.array(vec), k)
    return [texts[i] for i in I[0]]