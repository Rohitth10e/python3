from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(host="http://localhost:11432")

@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.get("/contact")
async def contact():
    return {"message": "rohith@mail.com"}

@app.post("/chat")
async def chat(
    user_message: str = Body(..., description="User message")
):
    response = client.chat(model="gemma:2b", messages=[
        {"role": "user", "content": user_message}
    ])
    return {"message": response["message"]["content"]}