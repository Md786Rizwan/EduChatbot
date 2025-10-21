import tensorflow as tf
import numpy as np

# Simple GAN for generating advice-vectors mapped to advice text

class Generator(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.dense1 = tf.keras.layers.Dense(32, activation='relu')
        self.dense2 = tf.keras.layers.Dense(10, activation='tanh')
    def call(self, x):
        x = self.dense1(x)
        return self.dense2(x)

class Discriminator(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.dense1 = tf.keras.layers.Dense(32, activation='relu')
        self.dense2 = tf.keras.layers.Dense(1, activation='sigmoid')
    def call(self, x):
        x = self.dense1(x)
        return self.dense2(x)

def generate_synthetic_advice():
    # Generator and Discriminator for demo purposes (not fully trained)
    generator = Generator()
    noise = tf.random.normal([1, 10])
    advice_vector = generator(noise).numpy().flatten()
    advice_options = [
        "You are capable of amazing things.",
        "Take small steps each day.",
        "Keep an open mind and heart.",
        "Learning from mistakes leads to growth.",
        "Stay focused on your goals.",
        "Support and care for others.",
        "Express gratitude daily.",
        "Balance study with relaxation.",
        "Ask questions and seek understanding.",
        "Celebrate your victories!"
    ]
    # Pick advice based on peak value in advice_vector for variety
    idx = int(np.argmax(advice_vector)) % len(advice_options)
    return advice_options[idx]
