from answer_query import answer_query


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

user_question = "What is an Array in Javascript?"
answer = answer_query(user_question)
print("Answer:", answer)
