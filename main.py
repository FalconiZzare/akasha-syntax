from prints.print_green import print_green
from utils.calculate_cosine_similarity import calculate_cosine_similarity
from utils.generate_response import generate_response
from utils.generate_response_local import generate_response_local
from utils.index_documents import setup_chromadb, query_retriever

# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

# setup_chromadb()

user_input = "What is an object in javascript?"
relevant_chunks = query_retriever(user_input)

# Qwen
# response = generate_response(user_input, relevant_chunks)
# print_green(" Generated Response:")
# print(response)

#DeepSeekDistillQwen
# response = generate_response(user_input, relevant_chunks, model_index=4)
# print_green(" Generated Response DeepSeek Distill:")
# print(response)

# DeepSeek R1 7B
# response = generate_response_local(user_input, relevant_chunks)
# print_green(" Generated Response DeepSeek:")
# print(response)
