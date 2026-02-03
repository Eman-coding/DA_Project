"""
Train ML Model for Fake Review Detection
Simple embedding + dense layers architecture
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os

np.random.seed(42)
tf.random.set_seed(42)

MAX_WORDS = 1000
MAX_LEN = 50
EMBEDDING_DIM = 16
EPOCHS = 20
BATCH_SIZE = 8

def load_data():
    """Load training data"""
    df = pd.read_csv('data/train.csv')
    reviews = df['review'].values
    labels = df['label'].map({'real': 0, 'fake': 1}).values
    return reviews, labels

def preprocess_data(reviews, labels):
    """Tokenize and pad reviews"""
    tokenizer = Tokenizer(num_words=MAX_WORDS, oov_token="<OOV>")
    tokenizer.fit_on_texts(reviews)
    
    sequences = tokenizer.texts_to_sequences(reviews)
    padded = pad_sequences(sequences, maxlen=MAX_LEN, padding='post', truncating='post')
    
    return padded, labels, tokenizer

def build_model():
    """Build lightweight model"""
    model = keras.Sequential([
        keras.layers.Embedding(MAX_WORDS, EMBEDDING_DIM, input_length=MAX_LEN),
        keras.layers.GlobalAveragePooling1D(),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train():
    """Train the model"""
    print("Loading data...")
    reviews, labels = load_data()
    print(f"Loaded {len(reviews)} reviews")
    
    print("Preprocessing...")
    X, y, tokenizer = preprocess_data(reviews, labels)
    
    split_idx = int(0.8 * len(X))
    X_train, X_val = X[:split_idx], X[split_idx:]
    y_train, y_val = y[:split_idx], y[split_idx:]
    
    print(f"Training: {len(X_train)}, Validation: {len(X_val)}")
    
    print("Building model...")
    model = build_model()
    
    print("Training...")
    model.fit(X_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE,
              validation_data=(X_val, y_val), verbose=1)
    
    loss, accuracy = model.evaluate(X_val, y_val, verbose=0)
    print(f"Validation Accuracy: {accuracy:.4f}")
    
    os.makedirs('models', exist_ok=True)
    model.save('models/review_model.h5')
    
    with open('models/tokenizer.pkl', 'wb') as f:
        pickle.dump(tokenizer, f)
    
    print("Model saved to models/review_model.h5")
    print("Tokenizer saved to models/tokenizer.pkl")

if __name__ == '__main__':
    train()
