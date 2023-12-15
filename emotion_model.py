# emotion_model.py
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib as jb

class EmotionModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = SVC(kernel='linear')
        self.is_fitted = False  # Flag to track whether the model is fitted

    def fit_vectorizer(self, X):
        try:
            self.vectorizer.fit(X)
            self.is_fitted = True
        except Exception as e:
            print(f"Error fitting the TF-IDF vectorizer: {str(e)}")
            raise  # Reraise the exception for better debugging

    def fit_model(self, X, y):
        try:
            X_tfidf = self.vectorizer.transform(X)
            self.model.fit(X_tfidf, y)
        except Exception as e:
            print(f"Error fitting the SVM model: {str(e)}")
            raise  # Reraise the exception for better debugging

    def train(self, X, y):
        try:
            self.fit_vectorizer(X)
            self.fit_model(X, y)
        except Exception as e:
            print(f"Error during training: {str(e)}")
            raise  # Reraise the exception for better debugging

    def predict(self, text):
        try:
            if not text:
                raise ValueError("Empty input text")

            # Ensure that the model and vectorizer are fitted
            if not self.is_fitted:
                raise ValueError("TF-IDF vectorizer and SVM model are not fitted. Train the model first.")

            text_tfidf = self.vectorizer.transform([text])
            prediction = self.model.predict(text_tfidf)
            return prediction[0]
        except Exception as e:
            print(f"Error predicting emotion: {str(e)}")
            raise  # Reraise the exception for better debugging

    def save_model(self, filename='emotion_model.pkl'):
        try:
            jb.dump((self.vectorizer, self.model), filename)
            print("Model saved successfully.")
        except Exception as e:
            print(f"Error saving model: {str(e)}")
            raise  # Reraise the exception for better debugging

    def load_model(self, filename='emotion_model.pkl'):
        try:
            if os.path.exists(filename):
                loaded_vectorizer, loaded_model = jb.load(filename)
                self.vectorizer = loaded_vectorizer
                self.model = loaded_model
                self.is_fitted = True
                print("Model loaded successfully.")
            else:
                print(f"Error: Model file '{filename}' not found.")
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise  # Reraise the exception for better debugging
