from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests, json

app = FastAPI()

# Allow frontend (HTML) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:5500"] if you serve frontend locally
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

def ask_ollama(prompt: str) -> str:
    payload = {"model": "llama3", "prompt": prompt}
    response = requests.post(OLLAMA_URL, json=payload, stream=True)

    result = ""
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    result += data["response"]
            except Exception as e:
                print("Error parsing line:", e)
    return result

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask")
async def ask(req: PromptRequest):
    response = ask_ollama(req.prompt)
    return {"response": response}










