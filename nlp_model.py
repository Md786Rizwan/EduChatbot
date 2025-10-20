from transformers import pipeline

# Load a conversational pipeline for dialogue (from Hugging Face)
chatbot_pipeline = pipeline("conversational", model="microsoft/DialoGPT-medium")

def get_counseling_response(user_input):
    try:
        response = chatbot_pipeline(user_input)
        # Extract answer text from pipeline's response
        if isinstance(response, list):
            return response[0]['generated_text']
        return str(response)
    except Exception as e:
        return "I'm here to help, can you ask in a different way?"
