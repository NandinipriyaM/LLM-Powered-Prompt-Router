import os
import ollama
from .prompts import EXPERT_PROMPTS

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

client = ollama.Client(host=OLLAMA_HOST)

def route_and_respond(message: str, intent: str) -> str:
    if intent == "unclear":
        return ("I'm sorry, I couldn't determine your intent. Could you please clarify "
                "what you need help with? (e.g., coding, data analysis, writing, career advice)")

    system_prompt = EXPERT_PROMPTS.get(intent)
    if not system_prompt:
        return "I'm not sure how to help with that. Please try rephrasing."

    try:
        response = client.chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            options={"temperature": 0.7}
        )
        return response["message"]["content"]
    except Exception as e:
        return f"An error occurred: {str(e)}"