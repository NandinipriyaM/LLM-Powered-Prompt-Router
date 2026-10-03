from flask import Flask, request, jsonify
from app.main import process_message

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "LLM-Powered Prompt Router API is running"
    })


@app.route("/api", methods=["POST"])
def route_prompt():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({
            "error": "Please provide a 'message' field"
        }), 400

    message = data["message"]

    intent, confidence, response = process_message(message)

    return jsonify({
        "message": message,
        "intent": intent,
        "confidence": confidence,
        "response": response
    })