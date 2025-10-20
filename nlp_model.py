from transformers import pipeline

# Load Question Answering pipeline
qa_pipeline = pipeline("question-answering")

def get_counseling_response(user_input):
    educational_context = (
        "Students often need help with career planning, stress management, "
        "study tips, and goal setting. As a counselor, provide clear, practical advice."
    )
    try:
        output = qa_pipeline(question=user_input, context=educational_context)
        return output["answer"]
    except:
        return "Sorry, I'm still learning! Please rephrase your question."
