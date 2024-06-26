from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Dialogflow endpoint and headers
url = "https://dialogflow.googleapis.com/v2/projects/mindme-427009/agent/sessions/f94b87d7-0ced-9e5a-e05c-86e3a2f2a246:detectIntent"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer ya29.a0AXooCgtwDI6AOOWlcSysL7L9OKKjjjEsniLSCCSQ7krKtj3W5oorMrH7GzDbmKJVhwCurOv6FPVmN8jF8CPjUEnqzkvMWtLYL-vEkZoPJ688vBZxoSvFNnuA1JgMbe3yK4zym6PwoIjC-K8mzCDTAFBWS7ZIRVuq6mKyjEP_QjLs5iwnVy8lzo7X0MwqeKZxrmD-IHBh2z0H4yRAuyfkdVS2Dzdhcc6XEGcXmdlbBT4nwhfm1T8SByP2gUure0CdNDl47cEdD2O1LOlGd6rDRHyVKwZzLA7L3a97yd-e_mL-Ym0d4XT-DFoRkcMm81ugWmcmbuaiEgQur4cnOoAYZs5Os2Ebk-tlwUsL2f62Q8EheuJLF5hjsDwvqJzgBuSkHXmj3iYpXhxepYXXB8ulRRJ2-FooXFRCMSDagwaCgYKARcSARASFQHGX2MiAJSugzlOdgbrAY4xl6RK6g0429"
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
    return jsonify({
        'input_text': input_text,
        'intent': intent,
        'fulfillment': fulfillment
    })

if __name__ == '__main__':
    app.run(debug=True)
