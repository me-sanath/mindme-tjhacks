import requests
import json

url = "https://dialogflow.googleapis.com/v2/projects/mindme-427009/agent/sessions/f94b87d7-0ced-9e5a-e05c-86e3a2f2a246:detectIntent"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer ya29.a0AXooCgtwDI6AOOWlcSysL7L9OKKjjjEsniLSCCSQ7krKtj3W5oorMrH7GzDbmKJVhwCurOv6FPVmN8jF8CPjUEnqzkvMWtLYL-vEkZoPJ688vBZxoSvFNnuA1JgMbe3yK4zym6PwoIjC-K8mzCDTAFBWS7ZIRVuq6mKyjEP_QjLs5iwnVy8lzo7X0MwqeKZxrmD-IHBh2z0H4yRAuyfkdVS2Dzdhcc6XEGcXmdlbBT4nwhfm1T8SByP2gUure0CdNDl47cEdD2O1LOlGd6rDRHyVKwZzLA7L3a97yd-e_mL-Ym0d4XT-DFoRkcMm81ugWmcmbuaiEgQur4cnOoAYZs5Os2Ebk-tlwUsL2f62Q8EheuJLF5hjsDwvqJzgBuSkHXmj3iYpXhxepYXXB8ulRRJ2-FooXFRCMSDagwaCgYKARcSARASFQHGX2MiAJSugzlOdgbrAY4xl6RK6g0429"
}

data = {
    "queryInput": {
        "text": {
            "text": "im feeling depressed rn",
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

# Make the POST request
response = requests.post(url, headers=headers, data=json_data)

def extract_intent_and_fulfillment(response):
    response = response.json()
    intent_name = response['queryResult']['intent']['displayName']
    fulfillment_text = response['queryResult']['fulfillmentText']
    return intent_name, fulfillment_text

# Print the response
print(extract_intent_and_fulfillment(response))
