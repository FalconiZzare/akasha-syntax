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

setup_chromadb()

user_input = "What is an array in Javascript?"
relevant_chunks = query_retriever(user_input)

# #Qwen/Qwen1.5-0.5B-Chat
response = generate_response(user_input, relevant_chunks)
print(f"Generated Response Qwen: {response}")

# DeepSeek R1 7B
# response = generate_response_local(user_input, relevant_chunks)
# print(f"Generated Response DeepSeek: {response}")
