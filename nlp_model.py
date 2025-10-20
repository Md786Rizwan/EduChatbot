from transformers import pipeline

chatbot_pipeline = pipeline("conversational", model="microsoft/DialoGPT-medium")
sentiment_pipeline = pipeline("sentiment-analysis")

def get_counseling_response(user_input):
    try:
        sentiment = sentiment_pipeline(user_input)[0]
        response = chatbot_pipeline(user_input)
        if isinstance(response, list):
            chat_out = response[0]['generated_text']
        else:
            chat_out = str(response)
        return f"{chat_out} (Your mood seems: {sentiment['label']})"
    except Exception as e:
        return "I'm here to help, can you ask in a different way?"
