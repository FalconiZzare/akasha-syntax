from utils.calculate_cosine_similarity import calculate_cosine_similarity


def generate_response(query, context_chunks, threshold=0.5, similarity_rate=20):
    import re
    from utils.model_singleton import ModelSingleton

    identity_patterns = [
        r"who\s+are\s+you",
        r"what\s+are\s+you",
        r"introduce\s+yourself",
        r"tell\s+me\s+about\s+yourself"
    ]

    is_identity_question = any(re.search(pattern, query.lower()) for pattern in identity_patterns)

    if not is_identity_question:
        similarity_scores = calculate_cosine_similarity(query, context_chunks)
        count_above_threshold = sum(score >= threshold for score in similarity_scores)
        percentage_above_threshold = (count_above_threshold / len(similarity_scores)) * 100

        if percentage_above_threshold <= similarity_rate:
            return "⚠️ Sorry, I couldn't find relevant information to answer your question."

    model_instance = ModelSingleton.get_instance()

    context = "\n".join(context_chunks)

    # For identity questions, use a more specific prompt
    if is_identity_question:
        messages = [
            {"role": "user",
             "content": f"Use the following context to introduce yourself as the AI assistant:\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer as if you are the assistant described in the context:"}
        ]
    else:
        messages = [
            {"role": "user",
             "content": f"Use ONLY the following context to answer the question:\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"}
        ]

    response = model_instance.generate(messages)
    return response