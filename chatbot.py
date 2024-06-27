from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Dialogflow endpoint and headers
url = "https://dialogflow.googleapis.com/v2/projects/mindme-427009/agent/sessions/f94b87d7-0ced-9e5a-e05c-86e3a2f2a246:detectIntent"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer ya29.a0AXooCgta84DPHRXk0XyfRhWibJM1Al6tn1Lrvuo9xul0VJWCTH0x40hQq1EeTsJtnL7bTEUtsujsJ2xhK7QphT5pmPOGezT1trPEGDzNOG3zE_JNP5qh0cEyI8qwwgv-R3TTNS47aGMXU9Yi0LeoK0o-Mx4LxoDgibW6ZSyauyDdG0slHN5xAskU3vli76iN5lsEOIL_J9N0PPN7jEQlhJH-ox962SRyyq2ZgMNltwpCh_eks6wl6bnhKLgJXQm2RXSJcatWh7ls34tZaGlmTJqPjvlS9p_qM5pFhvz3EOfsBh9vtwud-iWQaoi-ZmoR950EN9USrANDBCAsIveykomwOzDhHEA-u52JHNGEmAPqb8GTNY42ly3NlTG_7S6yU2u3pqY5yXQjk2tPD1RWnpVR5rwQhh65ir6bLSYaCgYKAdASARASFQHGX2MirbyzIdh81ktfp-jFJ6a-0g0430"
}

def detect_intent(text):
    # Create request data for Dialogflow
    data = {
        "queryInput": {
            "text": {
                "text": text,
                "languageCode": "en"
            }
        },
        "queryParams": {
            "source": "DIALOGFLOW_CONSOLE",
            "timeZone": "Asia/Calcutta"
        }
    }

    # Convert data to JSON format
    json_data = json.dumps(data)

    # Make the POST request to Dialogflow
    response = requests.post(url, headers=headers, data=json_data)

    # Parse the response and extract intent and fulfillment text
    if response.status_code == 200:
        response_json = response.json()
        intent_name = response_json['queryResult']['intent']['displayName']
        fulfillment_text = response_json['queryResult']['fulfillmentText']
        return intent_name, fulfillment_text
    else:
        print(response)
        return None, "Error: Unable to process request"

@app.route('/query', methods=['POST'])
def query():
    # Extract text from the request
    request_data = request.get_json()
    input_text = request_data.get('text')

    if not input_text:
        return jsonify({'error': 'No input text provided'}), 400

    # Call detect_intent function to get intent and fulfillment text
    intent, fulfillment = detect_intent(input_text)

    # Return JSON response
    response = jsonify({
        'input_text': input_text,
        'intent': intent,
        'fulfillment': fulfillment
    })
    # Set CORS headers for the response
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')

    return response

if __name__ == '__main__':
    app.run(debug=True)


