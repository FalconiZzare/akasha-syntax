import os
import shutil

import chromadb
from sentence_transformers import SentenceTransformer

from utils.load_documents import load_documents
from prints.print_green import print_green
from prints.print_red import print_red
from utils.text_splitter import text_splitter


def setup_chromadb():
    docs = load_documents("datasets")

    print_green("Setting up ChromaDB...")

    # Delete existing content of ChromaDB folder
    try:
        chroma_db_path = "chroma_db"
        if os.path.exists(chroma_db_path):
            for file_name in os.listdir(chroma_db_path):
                file_path = os.path.join(chroma_db_path, file_name)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

        print_red("Deleted existing ChromaDB folder contents.")
    except Exception as e:
        print_red(f"Could not delete chroma db path: {e}")

    client = chromadb.PersistentClient(path="chroma_db")
    text_embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    # Delete existing collection
    try:
        client.delete_collection(name="knowledge_base")
        print_red("Deleted existing collection: knowledge_base")
    except Exception as e:
        print_red(f"{e}")

    collection = client.create_collection(name="knowledge_base")

    # Iterating through docs array processing their own chunks
    print_green("Chunking and embedding documents...")
    for i, doc in enumerate(docs):
        print_green(f"Processing document: {i + 1} of {len(docs)}")
        chunks = text_splitter(doc)

        for j, chunk in enumerate(chunks):
            embedding = text_embedding_model.encode(chunk)
            collection.add(
                ids=[f"doc_{i}_chunk_{j}"],
                documents=[chunk],
                embeddings=[embedding],
                metadatas=[{"source": "txt", "chunk_id": f"doc_{i}_chunk_{j}"}],
            )
    print_green("Text chunks and embeddings stored in ChromaDB.")

    return collection


def query_retriever(query, top_k=3):
    text_embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = text_embedding_model.encode(query).tolist()

    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_collection(name="knowledge_base")

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    relevant_chunks = [chunk for sublist in results["documents"] for chunk in sublist]
    return relevant_chunks
