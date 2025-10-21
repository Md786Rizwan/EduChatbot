from gan_model import generate_gan_response

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    # ... (Get NLP or dataset response as before)
    gan_response = generate_gan_response(user_input)
    return jsonify({
        "nlp_response": nlp_response,      # From your NLP model/dataset
        "gan_response": gan_response       # NEW: From your GAN generator
    })
