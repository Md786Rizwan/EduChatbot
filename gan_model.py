import tensorflow as tf
import random
def generate_synthetic_advice():
    # Minimal GAN Generator (for demonstration)
    noise = tf.random.normal([1, 10])
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(16, activation='relu', input_shape=(10,)),
        tf.keras.layers.Dense(1, activation='tanh')
    ])
    synthetic = model(noise).numpy()[0,0]
    # Map synthetic value to example advice
    advice_options = [
        "Believe in your strengths!",
        "Consistency is the key.",
        "Never hesitate to ask for help.",
        "Keep your goals flexible.",
        "Stay curious and keep learning."
        "It’s okay to make mistakes—learn from them.",
        "Balance work and rest for best results.",
        "Reach out if you feel overwhelmed.",
        "Try breaking big tasks into smaller steps.",
        "Confidence comes from practice—keep trying!"
    ]
    return advice_options[int(abs(synthetic)*len(advice_options)) % len(advice_options)]
