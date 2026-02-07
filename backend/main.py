from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Allow requests from your frontend (file:// works too)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only. Later restrict to your domain
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

@app.post("/chat")
def chat(message: dict):
    r = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": message["text"],
            "stream": False
        }
    )
    return {"reply": r.json()["response"]}
