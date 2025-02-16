import ollama
import re


def generate_response_local(query, context_chunks):
    model_name = "deepseek-r1"

    # Format the prompt with query and context
    context = "\n".join(context_chunks)
    prompt = (
        "You are an assistant. Use the following context to answer the question:\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n\nAnswer:"
    )

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",
         "content": f"Use ONLY the following context to answer the question:\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"}
    ]

    # Generate the response using Ollama
    response = ollama.chat(
        model=model_name,
        messages=messages,
    )

    response_content = response['message']['content']
    final_answer = re.sub(r'<think>.*?</think>', '', response_content, flags=re.DOTALL).strip()
    return final_answer
