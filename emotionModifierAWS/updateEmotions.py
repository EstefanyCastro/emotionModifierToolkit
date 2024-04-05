from restrictions import (
    validate_emotional_entity_length,
    validate_emotions,
    validate_pad_values,
)


def update_emotions(
    emotional_entity,
    happiness_amount,
    sadness_amount,
    fear_amount,
    anger_amount,
    disgust_amount,
    surprise_amount,
):
    """
    Increases or decrease the emotions in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        happiness_amount (int): The amount of happiness mutation.
        sadness_amount (int): The amount of sadness mutation.
        fear_amount (int): The amount of fear mutation.
        anger_amount (int): The amount of anger mutation.
        disgust_amount (int): The amount of disgust mutation.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: An error message.
    """
    error_length = validate_emotional_entity_length(emotional_entity)
    if error_length:
        return error_length

    if len(emotional_entity) == 6 or len(emotional_entity) == 9:
        emotional_entity[0] += happiness_amount
        emotional_entity[1] += sadness_amount
        emotional_entity[2] += fear_amount
        emotional_entity[3] += anger_amount
        emotional_entity[4] += disgust_amount
        emotional_entity[5] += surprise_amount

        error = validate_emotions(emotional_entity[:6])
        if error:
            return error

    return emotional_entity


def update_pad_values(
    emotional_entity, pleasure_amount, activation_amount, dominance_amount
):
    """
    Updates the PAD values in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        pleasure_amount (int): The amount of pleasure mutation.
        activation_amount (int): The amount of activation mutation.
        dominance_amount (int): The amount of dominance mutation.

    Returns:
        list: The updated emotional entity.
        str: An error message.
    """
    if len(emotional_entity) == 9:
        emotional_entity[6] += pleasure_amount
        emotional_entity[7] += activation_amount
        emotional_entity[8] += dominance_amount

        error = validate_pad_values(emotional_entity[6:])
        if error:
            return error

    return emotional_entity
