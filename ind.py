import json
import requests
from fastapi import FastAPI
from pydantic import BaseModel

# ------------------------------
# Ollama API Setup
# ------------------------------
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

def ask_ollama(prompt: str) -> str:
    """Send prompt to Ollama and get full response."""
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

def ask_ollama_stream(prompt: str) -> str:
    """Send prompt to Ollama and stream response live."""
    payload = {"model": "llama3", "prompt": prompt}
    response = requests.post(OLLAMA_URL, json=payload, stream=True)

    result = ""
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    chunk = data["response"]
                    print(chunk, end="", flush=True)  # Real-time streaming in terminal
                    result += chunk
            except Exception as e:
                print("Error parsing line:", e)
    print()  # final newline
    return result

# ------------------------------
# FastAPI Setup
# ------------------------------
app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = ask_ollama(req.prompt)  # change to ask_ollama_stream(req.prompt) if you want streaming
    return {"response": response}

# ------------------------------
# Terminal Interactive Chat
# ------------------------------
if __name__ == "__main__":
    print("Chat with AI (type 'exit' or 'quit' to stop)")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = ask_ollama(prompt)  # use ask_ollama_stream(prompt) for live streaming
        print("AI:", response)


