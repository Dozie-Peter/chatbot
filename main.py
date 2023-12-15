# main.py
import logging
from emotion_model import EmotionModel

def configure_logging():
    logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO

def main():
    configure_logging()

    # usage of EmotionModel
    emotion_model = EmotionModel()

    # Train the model with multi-class data
    training_data = ["I am happy, happiness, joy, joyous",  "I am sad, annoyed, angry, vexed", "You are excited", "They are surprised"]
    labels = ["happy", "sad", "excited", "surprised"]
    
    # Train the model
    emotion_model.train(training_data, labels)

    # Take user input
    user_input = input("Enter a sentence to analyze emotions: ")

    # Example: Predict using the model
    prediction = emotion_model.predict(user_input)
    print("Predicted Emotion:", prediction)

    # Example: Save and load the model
    emotion_model.save_model("my_model.pkl")
    loaded_model = EmotionModel()
    loaded_model.load_model("my_model.pkl")

if __name__ == "__main__":
    main()
