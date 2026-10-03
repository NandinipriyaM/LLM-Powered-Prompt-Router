# app/utils.py

import json
import re

def parse_classifier_response(raw: str) -> dict:
    """
    Parse the LLM response to extract intent and confidence.
    Expects a JSON string like {"intent": "code", "confidence": 0.95}
    If parsing fails, returns {"intent": "unclear", "confidence": 0.0}
    """
    # Try to find a JSON object in the response
    json_match = re.search(r'\{.*\}', raw, re.DOTALL)
    if json_match:
        try:
            data = json.loads(json_match.group())
            intent = data.get("intent", "unclear")
            confidence = float(data.get("confidence", 0.0))
            # Clamp confidence and ensure intent is allowed
            allowed_intents = {"code", "data", "writing", "career", "unclear"}
            if intent not in allowed_intents:
                intent = "unclear"
            confidence = max(0.0, min(1.0, confidence))
            return {"intent": intent, "confidence": confidence}
        except (json.JSONDecodeError, ValueError, TypeError):
            pass
    return {"intent": "unclear", "confidence": 0.0}