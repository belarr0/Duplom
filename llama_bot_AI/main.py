from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import ollama

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class ChatRequest(BaseModel):
    prompt: str

def query_llama(prompt: str) -> str:
    messages = [
        {"role": "system", "content": "Ти — корисний чат-бот для підтримки психічного здоров'я."},
        {"role": "user", "content": prompt}
    ]
    response = ollama.chat(model="llama2", messages=messages)
    return response["message"]["content"]

@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

@app.post("/chat")
async def chat(request: ChatRequest):
    response = query_llama(request.prompt)
    return {"response": response}
