import ollama
import re

from utils.calculate_cosine_similarity import calculate_cosine_similarity


def generate_response_local(query, context_chunks, threshold=0.5, similarity_rate=20):
    similarity_scores = calculate_cosine_similarity(query, context_chunks)
    count_above_threshold = sum(score >= threshold for score in similarity_scores)
    percentage_above_threshold = (count_above_threshold / len(similarity_scores)) * 100

    if percentage_above_threshold <= similarity_rate:
        return "⚠️ Sorry, I couldn't find relevant information to answer your question."

    model_name = "deepseek-r1"

    # Format the prompt with query and context
    context = "\n".join(context_chunks)
    prompt = (
        "You are an assistant. Use the following context to answer the question:\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n\nAnswer:"
    )

    messages = [
        {"role": "user",
         "content": f"<think>\nUse ONLY the following context to answer the question:\n\nContext:\n{context}\n\nQuestion: {query}"}
    ]

    # Generate the response using Ollama
    response = ollama.chat(
        model=model_name,
        messages=messages,
        stream=True
    )

    found_think_end = False  # Variable to track if </think> is found
    for chunk in response:
        if not found_think_end:
            if "</think>" in str(chunk):
                found_think_end = True
            continue

        print(chunk["message"]["content"], end="", flush=True)

    # response_content = response['message']['content']
    # # Remove the <think>...</think> part
    # response_content = re.sub(r'<think>.*?</think>', '', response_content, flags=re.DOTALL).strip()
    #
    # # Look for "Answer:" or "**Answer**" and extract the part after it
    # match = re.search(r'(?:\*\*Answer\*\*|Answer:|\*\*\*\*)\s*(.*)', response_content, re.DOTALL)
    #
    # return match.group(1).strip() if match else response_content.strip()
