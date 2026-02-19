import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, jsonify, session
from chatbot import get_response

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def home():
    session.pop("history", None)
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"reply": "Please type a message."})

    # Get conversation history from session
    history = session.get("history", [])

    # Get AI response
    reply = get_response(user_message, history)

    # Update history with this turn
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": reply})

    # Keep last 20 turns to avoid token overflow
    if len(history) > 40:
        history = history[-40:]

    session["history"] = history

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
