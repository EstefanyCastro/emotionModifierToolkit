import requests
import json


def call_lambda_function(endpoint, event):
    try:
        url_base = (
            "https://sgzan1udv6.execute-api.us-east-2.amazonaws.com/emotionModifier/"
        )
        response = requests.post(url_base + f"{endpoint}", json=event)

        if response.status_code == 200:
            lambda_response = json.loads(response.text)
            return lambda_response.get("body")
        else:
            return "Error calling Lambda function. Status code: " + str(
                response.status_code
            )

    except requests.exceptions.RequestException as e:
        return "Connection error: " + str(e)


def update_surprise(
    emotional_entity,
    surprise_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "updateSurprise"
    event = {
        "emotional_entity": emotional_entity,
        "surprise_amount": surprise_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def update_sadness(
    emotional_entity,
    sadness_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "updateSadness"
    event = {
        "emotional_entity": emotional_entity,
        "sadness_amount": sadness_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def update_positive_emotions(
    emotional_entity,
    happiness_amount,
    surprise_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "updatePositiveEmotions"
    event = {
        "emotional_entity": emotional_entity,
        "happiness_amount": happiness_amount,
        "surprise_amount": surprise_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def update_negative_emotions(
    emotional_entity,
    sadness_amount,
    fear_amount,
    anger_amount,
    disgust_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "updateNegativeEmotions"
    event = {
        "emotional_entity": emotional_entity,
        "sadness_amount": sadness_amount,
        "fear_amount": fear_amount,
        "anger_amount": anger_amount,
        "disgust_amount": disgust_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def update_happiness(
    emotional_entity,
    happiness_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "updateHappiness"
    event = {
        "emotional_entity": emotional_entity,
        "happiness_amount": happiness_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def update_fear(
    emotional_entity,
    fear_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "updateFear"
    event = {
        "emotional_entity": emotional_entity,
        "fear_amount": fear_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def update_disgust(
    emotional_entity,
    disgust_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "updateDisgust"
    event = {
        "emotional_entity": emotional_entity,
        "disgust_amount": disgust_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def update_anger(
    emotional_entity,
    anger_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "updateAnger"
    event = {
        "emotional_entity": emotional_entity,
        "anger_amount": anger_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def feel_shame(
    emotional_entity,
    fear_amount,
    disgust_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "feelShame"
    event = {
        "emotional_entity": emotional_entity,
        "fear_amount": fear_amount,
        "disgust_amount": disgust_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def feel_proud(
    emotional_entity,
    happiness_amount,
    anger_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "feelProud"
    event = {
        "emotional_entity": emotional_entity,
        "happiness_amount": happiness_amount,
        "anger_amount": anger_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def feel_jealous(
    emotional_entity,
    sadness_amount,
    anger_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "feelJealous"
    event = {
        "emotional_entity": emotional_entity,
        "sadness_amount": sadness_amount,
        "anger_amount": anger_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def feel_indignation(
    emotional_entity,
    anger_amount,
    surprise_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "feelIndignation"
    event = {
        "emotional_entity": emotional_entity,
        "anger_amount": anger_amount,
        "surprise_amount": surprise_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def feel_indifference(
    emotional_entity,
    anger_amount,
    disgust_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "feelIndifference"
    event = {
        "emotional_entity": emotional_entity,
        "anger_amount": anger_amount,
        "disgust_amount": disgust_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def feel_guilty(
    emotional_entity,
    happiness_amount,
    fear_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "feelGuilty"
    event = {
        "emotional_entity": emotional_entity,
        "happiness_amount": happiness_amount,
        "fear_amount": fear_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def feel_envy(
    emotional_entity,
    sadness_amount,
    anger_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "feelEnvy"
    event = {
        "emotional_entity": emotional_entity,
        "sadness_amount": sadness_amount,
        "anger_amount": anger_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def feel_disappointment(
    emotional_entity,
    sadness_amount,
    surprise_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "feelDisappointment"
    event = {
        "emotional_entity": emotional_entity,
        "sadness_amount": sadness_amount,
        "surprise_amount": surprise_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def feel_despair(
    emotional_entity,
    sadness_amount,
    fear_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "feelDespair"
    event = {
        "emotional_entity": emotional_entity,
        "sadness_amount": sadness_amount,
        "fear_amount": fear_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def feel_delight(
    emotional_entity,
    happiness_amount,
    surprise_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "feelDelight"
    event = {
        "emotional_entity": emotional_entity,
        "happiness_amount": happiness_amount,
        "surprise_amount": surprise_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def feel_alarm(
    emotional_entity,
    fear_amount,
    surprise_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "feelAlarm"
    event = {
        "emotional_entity": emotional_entity,
        "fear_amount": fear_amount,
        "surprise_amount": surprise_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def experience_natural_disaster(
    emotional_entity,
    sadness_amount,
    fear_amount,
    surprise_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "experienceNaturalDisaster"
    event = {
        "emotional_entity": emotional_entity,
        "sadness_amount": sadness_amount,
        "fear_amount": fear_amount,
        "surprise_amount": surprise_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def experience_injustice(
    emotional_entity,
    sadness_amount,
    fear_amount,
    anger_amount,
    surprise_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "experienceInjustice"
    event = {
        "emotional_entity": emotional_entity,
        "sadness_amount": sadness_amount,
        "fear_amount": fear_amount,
        "anger_amount": anger_amount,
        "surprise_amount": surprise_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def experience_crowd(
    emotional_entity,
    fear_amount,
    anger_amount,
    surprise_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "experienceCrowd"
    event = {
        "emotional_entity": emotional_entity,
        "fear_amount": fear_amount,
        "anger_amount": anger_amount,
        "surprise_amount": surprise_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def exciting_experience(
    emotional_entity,
    happiness_amount,
    surprise_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "excitingExperience"
    event = {
        "emotional_entity": emotional_entity,
        "happiness_amount": happiness_amount,
        "surprise_amount": surprise_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)


def be_criticized(
    emotional_entity,
    sadness_amount,
    anger_amount,
    surprise_amount,
    pleasure_amount=0,
    activation_amount=0,
    dominance_amount=0,
):
    endpoint = "beCriticized"
    event = {
        "emotional_entity": emotional_entity,
        "sadness_amount": sadness_amount,
        "anger_amount": anger_amount,
        "surprise_amount": surprise_amount,
        "pleasure_amount": pleasure_amount,
        "activation_amount": activation_amount,
        "dominance_amount": dominance_amount,
    }
    return call_lambda_function(endpoint, event)
