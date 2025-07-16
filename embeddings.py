from sentence_transformers import SentenceTransformer
import faiss, json, numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
with open("document_store/docs.json") as f:
    docs = json.load(f)

texts = [doc['content'] for doc in docs]
embeddings = model.encode(texts)
index = faiss.IndexFlatL2(embeddings[0].shape[0])
index.add(np.array(embeddings))

faiss.write_index(index, 'faiss.index')
with open('doc_texts.json', 'w') as f:
    json.dump(texts, f)