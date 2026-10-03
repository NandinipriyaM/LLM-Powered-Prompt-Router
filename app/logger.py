# app/logger.py

import json
from datetime import datetime

LOG_FILE = "route_log.jsonl"

def log_interaction(message: str, intent: str, confidence: float, response: str):
    """
    Append a log entry in JSON Lines format.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "intent": intent,
        "confidence": confidence,
        "message": message,
        "response": response
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")