import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path=".chromadb")
collection = client.get_or_create_collection("chapter_versions")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def save_version(chapter_id: str, stage: str, text: str):
    embedding = embedder.encode(text).tolist()
    vid = f"{chapter_id}_{stage}"
    collection.add(
        documents=[text],
        metadatas=[{"chapter_id": chapter_id, "stage": stage}],
        ids=[vid],
        embeddings=[embedding]
    )

def retrieve_similar(query: str, top_k: int = 3):
    q_emb = embedder.encode(query).tolist()
    res = collection.query(
        query_embeddings=[q_emb],
        n_results=top_k
    )
    return res["documents"][0], res["metadatas"][0]
