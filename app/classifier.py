import os
import ollama
from .utils import parse_classifier_response

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

client = ollama.Client(host=OLLAMA_HOST)

def classify_intent(message: str) -> dict:
    prompt = (
        "You are an intent classifier. Based on the user message below, choose only from the following labels: "
        "code, data, writing, career, unclear. Respond with a single JSON object containing two keys: "
        "'intent' (the label you chose) and 'confidence' (a float from 0.0 to 1.0, representing your certainty). "
        "Do not provide any other text or explanation.\n\n"
        f"User message: {message}"
    )

    try:
        response = client.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.0}
        )
        content = response["message"]["content"]
        return parse_classifier_response(content)
    except Exception as e:
        print(f"Classifier error: {e}")
        return {"intent": "unclear", "confidence": 0.0}