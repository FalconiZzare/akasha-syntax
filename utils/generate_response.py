from utils.calculate_cosine_similarity import calculate_cosine_similarity

def generate_response(query, context_chunks, threshold=0.5, similarity_rate=20):
    from utils.model_singleton import ModelSingleton

    similarity_scores = calculate_cosine_similarity(query, context_chunks)
    count_above_threshold = sum(score >= threshold for score in similarity_scores)
    percentage_above_threshold = (count_above_threshold / len(similarity_scores)) * 100

    if percentage_above_threshold <= similarity_rate:
        return "⚠️ Sorry, I couldn't find relevant information to answer your question."

    model_instance = ModelSingleton.get_instance()

    # Format the prompt with query and context
    context = "\n".join(context_chunks)
    messages = [
        {"role": "user",
         "content": f"Use ONLY the following context to answer the question:\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"}
    ]

    response = model_instance.generate(messages)

    return response