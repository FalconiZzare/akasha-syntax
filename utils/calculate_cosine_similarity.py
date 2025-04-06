def calculate_cosine_similarity(query, chunks):
    from utils.model_singleton import ModelSingleton

    model_instance = ModelSingleton.get_instance()

    # Compute the embedding for the query
    query_embedding = model_instance.encode_text([query])

    # Compute the embeddings for the chunks
    chunk_embeddings = model_instance.encode_text(chunks)

    # Calculate cosine similarity
    from sklearn.metrics.pairwise import cosine_similarity
    similarity_scores = cosine_similarity(query_embedding, chunk_embeddings)

    return similarity_scores.flatten().tolist()