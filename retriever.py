import numpy as np


def simple_retriever(index, embeddings_model, query, documents, k=1):
    # Get the query embedding
    query_embedding = embeddings_model.embed_query(query)

    # Ensure the query embedding has the correct shape
    query_embedding = np.array(query_embedding).astype('float32')

    # Perform the search using FAISS
    distances, indices = index.search(np.array([query_embedding]), k)

    # Handle case where indices might be out of range
    valid_indices = [i for i in indices[0] if i < len(documents)]  # Ensure all indices are valid

    # Ensure we don't get out-of-bounds error
    if len(valid_indices) < k:
        print(f"Warning: Not enough valid documents found, found {len(valid_indices)}.")

    # Retrieve and return the documents
    return [documents[i] for i in valid_indices]