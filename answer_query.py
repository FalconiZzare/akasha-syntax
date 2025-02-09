from index_documents import index_documents
from load_documents import load_documents
from model_configuration import get_prompt_template
from retriever import simple_retriever
import ollama

def answer_query(question):
    documents = load_documents("datasets/")
    index, embeddings_model = index_documents(documents)
    prompt_template = get_prompt_template()

    context = simple_retriever(index, embeddings_model, question, documents)

    combined_context = "n".join(context)

    response = ollama.generate(prompt_template.substitute(context=combined_context, question=question))

    return response.strip()