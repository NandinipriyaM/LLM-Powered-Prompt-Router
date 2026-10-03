import os
from flask import Flask, request, jsonify, render_template
from app.main import process_message

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


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