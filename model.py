"""
ML Model for Fake Review Detection
Lightweight TensorFlow/Keras implementation
"""

import os
import pickle
import numpy as np

# Lazy TensorFlow import
_tf_loaded = False
_keras = None
_pad_sequences = None

def _lazy_import_tf():
    """Import TensorFlow only when needed"""
    global _tf_loaded, _keras, _pad_sequences
    if not _tf_loaded:
        from tensorflow import keras
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        _keras = keras
        _pad_sequences = pad_sequences
        _tf_loaded = True
    return _keras, _pad_sequences

MAX_WORDS = 1000
MAX_LEN = 50

class ReviewPredictor:
    """Review prediction class"""
    
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.loaded = False
    
    def load_model(self):
        """Load trained model and tokenizer"""
        try:
            keras, _ = _lazy_import_tf()
            
            model_path = 'models/review_model.h5'
            tokenizer_path = 'models/tokenizer.pkl'
            
            if not os.path.exists(model_path) or not os.path.exists(tokenizer_path):
                raise FileNotFoundError("Model files not found. Run train_model.py first.")
            
            self.model = keras.models.load_model(model_path)
            
            with open(tokenizer_path, 'rb') as f:
                self.tokenizer = pickle.load(f)
            
            self.loaded = True
            print("Model loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def predict(self, review_text):
        """Predict if review is fake or real"""
        if not self.loaded:
            if not self.load_model():
                return None
        
        try:
            _, pad_sequences = _lazy_import_tf()
            
            sequence = self.tokenizer.texts_to_sequences([review_text])
            padded = pad_sequences(sequence, maxlen=MAX_LEN, padding='post', truncating='post')
            
            prediction = self.model.predict(padded, verbose=0)[0][0]
            
            fake_prob = float(prediction)
            real_prob = float(1 - prediction)
            
            label = "FAKE REVIEW" if fake_prob > 0.5 else "REAL REVIEW"
            
            return {
                'label': label,
                'fake_probability': fake_prob,
                'real_probability': real_prob
            }
        except Exception as e:
            print(f"Prediction error: {e}")
            return None

predictor = ReviewPredictor()
