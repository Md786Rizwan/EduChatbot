from flask import Flask, render_template, request, jsonify
from nlp_model import get_counseling_response
from gan_model import generate_synthetic_advice

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    nlp_response = get_counseling_response(user_input)
    synthetic_advice = generate_synthetic_advice()
    return jsonify({
        "nlp_response": nlp_response,
        "synthetic_advice": synthetic_advice
    })

if __name__ == "__main__":
    app.run(debug=True)
