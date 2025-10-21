import json, random, nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json', encoding='utf-8').read())

# Simple word processing
def clean_up(sentence):
    words = nltk.word_tokenize(sentence)
    words = [lemmatizer.lemmatize(w.lower()) for w in words]
    return words

def respond(user_input):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "I'm not sure I understand. Can you rephrase that?"
