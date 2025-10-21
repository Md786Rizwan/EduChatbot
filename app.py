from flask import Flask, render_template, request, jsonify
from model import respond
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"
LOG_FILE = "chat_logs.txt"

def save_log(user, bot):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | User: {user} | Bot: {bot}\n")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = respond(user_message)
    save_log(user_message, bot_reply)
    return jsonify({"response": bot_reply})

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    name = request.form.get("name")
    message = request.form.get("message")
    with open("feedback.txt", "a") as f:
        f.write(f"{name}: {message}\n")
    return render_template("feedback.html", success=True)

if __name__ == "__main__":
    app.run(debug=True)
