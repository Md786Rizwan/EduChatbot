import random

def generate_synthetic_advice():
    advice_options = [
        "Believe in your strengths!",
        "Consistency is the key.",
        "Never hesitate to ask for help.",
        "Keep your goals flexible.",
        "Stay curious and keep learning.",
        "It’s okay to make mistakes—learn from them.",
        "Balance work and rest for best results.",
        "Reach out if you feel overwhelmed.",
        "Try breaking big tasks into smaller steps.",
        "Confidence comes from practice—keep trying!"
    ]
    return random.choice(advice_options)
