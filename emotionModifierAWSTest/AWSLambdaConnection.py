import requests
import json


def call_lambda_function(url_api_gateway, event):
    try:
        response = requests.post(url_api_gateway, json=event)

        if response.status_code == 200:
            lambda_response = json.loads(response.text)
            return lambda_response.get("body")
        else:
            return "Error calling Lambda function. Status code: " + str(
                response.status_code
            )

    except requests.exceptions.RequestException as e:
        return "Connection error: " + str(e)


def update_happiness(
    emotional_entity,
    happiness_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    url_api_gateway = "https://sgzan1udv6.execute-api.us-east-2.amazonaws.com/emotionModifier/updateHappiness"
    event = {
        "emotional_entity": emotional_entity,
        "happiness_amount": happiness_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(url_api_gateway, event)
