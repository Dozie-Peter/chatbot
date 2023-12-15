# imports from flask, emotionmodel and logging
from flask import Flask, render_template, request, jsonify
from emotion_model import EmotionModel
import logging

app = Flask(__name__)
emotion_model = EmotionModel()

def configure_logging():
    logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_emotion', methods=['POST'])
def predict_emotion():
    try:
        data = request.json
        text = data.get('text', '')

        if not text:
            raise ValueError("Empty input text")

        # Train the model if not fitted
        if not emotion_model.is_fitted:
            # training data, if the user inputs any of these, the bot will predict the emotion with the corresponding emotion
            training_data = ["I am happy joyous joyful content pleased delighted cheerful overjoyed grateful", 
                             "I am sad unhappy dejected downcast disheartened blue gloomy", 
                             "You are confused bewildered disoriented perplexed puzzled disconcerted confounded"]
                             
            labels = ["happy", "sad", "confused"]
            emotion_model.train(training_data, labels)

        # Predict emotion using the model
        prediction = emotion_model.predict(text)

        return jsonify({'emotion': prediction})

    except Exception as e:
        error_message = f"Error predicting emotion: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message})

if __name__ == '__main__':
    configure_logging()
    app.run(debug=True)
