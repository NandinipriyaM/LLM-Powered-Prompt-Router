# app/main.py

import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from app.classifier import classify_intent
from app.router import route_and_respond
from app.logger import log_interaction

# The 15 test messages from the PDF
TEST_MESSAGES = [
    "how do i sort a list of objects in python?",
    "explain this sql query for me",
    "This paragraph sounds awkward, can you help me fix it?",
    "I'm preparing for a job interview, any tips?",
    "what's the average of these numbers: 12, 45, 23, 67, 34",
    "Help me make this better.",
    "I need to write a function that takes a user id and returns their profile, but also i need help with my resume.",
    "hey",
    "Can you write me a poem about clouds?",
    "Rewrite this sentence to be more professional.",
    "I'm not sure what to do with my career.",
    "what is a pivot table",
    "fix this bug pls: for i in range(10) print(i)",
    "How do I structure a cover letter?",
    "My boss says my writing is too verbose."
]

def process_message(message: str):
    """Classify, route, log, and return intent+confidence+response."""
    intent_data = classify_intent(message)
    intent = intent_data["intent"]
    confidence = intent_data["confidence"]

    response = route_and_respond(message, intent)

    log_interaction(message, intent, confidence, response)
    return intent, confidence, response

if __name__ == "__main__":
    print("Starting prompt router with 15 test messages...\n")
    for i, msg in enumerate(TEST_MESSAGES, 1):
        print(f"--- Test {i} ---")
        print(f"Message: {msg}")
        intent, conf, resp = process_message(msg)
        print(f"Intent: {intent} (confidence: {conf:.2f})")
        # Show first 200 chars of response
        preview = resp[:200] + "..." if len(resp) > 200 else resp
        print(f"Response preview: {preview}\n")

    print("All done. Check route_log.jsonl for the full log.")