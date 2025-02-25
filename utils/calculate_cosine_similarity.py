from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_cosine_similarity(query, chunks):
    # Load the SentenceTransformer model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Compute the embedding for the query
    query_embedding = model.encode([query])

    # Compute the embeddings for the chunks
    chunk_embeddings = model.encode(chunks)

    # Calculate cosine similarity between the query embedding and each chunk embedding
    similarity_scores = cosine_similarity(query_embedding, chunk_embeddings)

    # Flatten the similarity scores to a 1D array
    similarity_scores = similarity_scores.flatten()

    return similarity_scores.tolist()