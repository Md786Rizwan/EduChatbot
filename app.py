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

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    success = False
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        with open("feedback.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} | {name}: {message}\n")
        success = True
    return render_template("feedback.html", success=success)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = respond(user_message)
    save_log(user_message, bot_reply)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
