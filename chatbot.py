from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load a pre-trained model and tokenizer from Hugging Face
nlp = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_response(user_input):
    # Use the model to classify the sentiment of the input
    result = nlp(user_input)
    sentiment = result[0]['label']

    # Generate a response based on the sentiment
    if sentiment == 'POSITIVE':
        return "That's great to hear! Keep up the positive outlook."
    elif sentiment == 'NEGATIVE':
        return "I'm sorry to hear that. It's okay to have off days. Take some time for self-care."
    else:
        return "I'm here to help with mental health concerns. Can you tell me more about how you're feeling?"

@app.route('/query', methods=['POST'])
def query():
    request_data = request.get_json()
    input_text = request_data.get('text')

    if not input_text:
        return jsonify({'error': 'No input text provided'}), 400

    fulfillment = get_response(input_text)

    response = jsonify({
        'input_text': input_text,
        'fulfillment': fulfillment
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')

    return response

@app.route('/')
def home():
    return "Welcome to the MindMe Assistant! Use the /query endpoint to interact with the chatbot."

if __name__ == '__main__':
    app.run(debug=True)
