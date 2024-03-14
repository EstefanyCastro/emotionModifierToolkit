import json
from functions import *
from restrictions import *
from updateEmotions import *


def lambda_handler(event, context):
    # Gets the event parameters
    function_to_call = event.get("function_to_call", str)
    emotional_entity = event.get("emotional_entity", [])
    happiness_amount = event.get("happiness_amount", 0)
    sadness_amount = event.get("sadness_amount", 0)
    fear_amount = event.get("fear_amount", 0)
    anger_amount = event.get("anger_amount", 0)
    disgust_amount = event.get("disgust_amount", 0)
    surprise_amount = event.get("surprise_amount", 0)
    pleasure_amount = event.get("pleasure_amount", 0)
    activation_amount = event.get("activation_amount", 0)
    dominance_amount = event.get("dominance_amount", 0)

    # Validates the emotional entity
    validation_error = validate_emotional_entity(emotional_entity)
    if validation_error:
        return {"statusCode": 400, "body": validation_error}

    # Validates amounts
    validation_error = validate_amounts(
        pleasure_amount,
        activation_amount,
        dominance_amount,
        happiness_amount,
        sadness_amount,
        fear_amount,
        anger_amount,
        disgust_amount,
        surprise_amount,
    )
    if validation_error:
        return {"statusCode": 400, "body": validation_error}

    # Dictionary mapping function names to their corresponding update functions
    update_functions = {
        "updateHappiness": lambda: update_happiness(emotional_entity, happiness_amount),
        "updateSadness": lambda: update_sadness(emotional_entity, sadness_amount),
        "updateFear": lambda: update_fear(emotional_entity, fear_amount),
        "updateAnger": lambda: update_anger(emotional_entity, anger_amount),
        "updateDisgust": lambda: update_disgust(emotional_entity, disgust_amount),
        "updateSurprise": lambda: update_surprise(emotional_entity, surprise_amount),
        "updatePositiveEmotions": lambda: update_positive_emotions(
            emotional_entity, happiness_amount, surprise_amount
        ),
        "updateNegativeEmotions": lambda: update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        ),
        "updateFeelShame": lambda: update_feel_shame(
            emotional_entity, fear_amount, disgust_amount
        ),
        "updateFeelProud": lambda: update_feel_proud(
            emotional_entity, happiness_amount, anger_amount
        ),
        "updateFeelJealous": lambda: update_feel_jealous(
            emotional_entity, sadness_amount, anger_amount
        ),
        "updateFeelIndignation": lambda: update_feel_indignation(
            emotional_entity, anger_amount, surprise_amount
        ),
        "updateFeelIndiference": lambda: update_feel_indiference(
            emotional_entity, anger_amount, disgust_amount
        ),
        "updateFeelGuilty": lambda: update_feel_guilty(
            emotional_entity, happiness_amount, fear_amount
        ),
        "updateFeelEnvy": lambda: update_feel_envy(
            emotional_entity, sadness_amount, anger_amount
        ),
        "updateFeelDisappointment": lambda: update_feel_disappointment(
            emotional_entity, sadness_amount, surprise_amount
        ),
        "updateFeelDespair": lambda: update_feel_despair(
            emotional_entity, sadness_amount, fear_amount
        ),
        "updateFeelDelight": lambda: update_feel_delight(
            emotional_entity, happiness_amount, surprise_amount
        ),
        "updateFeelAlarm": lambda: update_feel_alarm(
            emotional_entity, fear_amount, surprise_amount
        ),
        "updateExperienceNaturalDisaster": lambda: update_experience_natural_disaster(
            emotional_entity, sadness_amount, fear_amount, surprise_amount
        ),
        "updateExperienceInjustice": lambda: update_experience_injustice(
            emotional_entity, sadness_amount, fear_amount, anger_amount, surprise_amount
        ),
        "updateExperienceCrowd": lambda: update_experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        ),
        "updateExcitingExperience": lambda: update_exciting_experience(
            emotional_entity, happiness_amount, surprise_amount
        ),
        "updateBeCritized": lambda: update_be_criticized(
            emotional_entity, sadness_amount, anger_amount, surprise_amount
        ),
    }

    # Check if the function to call is in the update functions dictionary
    if function_to_call in update_functions:
        # Call the corresponding update function
        updated_emotional_entity = update_functions[function_to_call]()
    else:
        return {"statusCode": 400, "body": "Invalid function to call"}

    # Update PAD values
    if len(emotional_entity) == 9:
        updated_emotional_entity = update_pad_values(
            updated_emotional_entity,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )
        if isinstance(updated_emotional_entity, str):
            return {"statusCode": 400, "body": updated_emotional_entity}

    # Returns the updated emotional entity
    return {"statusCode": 200, "body": updated_emotional_entity}
