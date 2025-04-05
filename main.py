from contextlib import asynccontextmanager

from prints.print_green import print_green, print_green_text
from prints.print_red import print_red
from utils.calculate_cosine_similarity import calculate_cosine_similarity
from utils.generate_response import generate_response
from utils.generate_response_local import generate_response_local
from utils.index_documents import setup_chromadb, query_retriever

from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_chromadb()
    print_green("🚀 Server started")

    yield
    print_red("🛑 Server shutting down")

app = FastAPI(
    title="Akasha Syntax",
    description="Akasha Syntax Query Endpoint",
    lifespan=lifespan
)

@app.get("/")
async def root():
    return {"message": "Akasha Syntax is running", "status": "ok"}


@app.post("/ask")
async def ask_question(query: str = Form(...)):
    try:
        print_green_text(f"#query: {query}")
        relevant_chunks = query_retriever(query)

        response = generate_response(query, relevant_chunks)

        print(response)

        return JSONResponse(content={
            "query": query,
            "response": response,
        })

    except Exception as e:
        print(f"Error processing query: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "message": "Failed to process query",
            }
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

# Qwen
# response = generate_response(user_input, relevant_chunks)
# print_green_text(f"#query: {user_input}")
# print_green(" Qwen:")
# print(response)
#
# # DeepSeekDistillQwen
# response = generate_response(user_input, relevant_chunks)
# print_green_text(f"#query: {user_input}")
# print_green(" Qwen 2.5:")
# print(response)

# DeepSeek R1 7B
# print_green_text(f"#query: {user_input}")
# print_green(" DeepSeek:")
# generate_response_local(user_input, relevant_chunks)
