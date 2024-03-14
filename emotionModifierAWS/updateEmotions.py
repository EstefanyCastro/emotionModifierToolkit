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
        str: An error response if the total emotion sum exceeds 100.
    """

    if len(emotional_entity) == 6 or len(emotional_entity) == 9:
        emotional_entity[0] += happiness_amount
        emotional_entity[1] += sadness_amount
        emotional_entity[2] += fear_amount
        emotional_entity[3] += anger_amount
        emotional_entity[4] += disgust_amount
        emotional_entity[5] += surprise_amount

        for i in emotional_entity[:6]:
            if i < 0:
                return "The emotional entity update cannot have negative emotions"

        total_emotions_sum = sum(emotional_entity[:6])
        if total_emotions_sum > 100:
            return "The total sum of emotions cannot exceed 100"

    else:
        return "The list of emotions must have 6 positions for the Paul Ekman model or 9 positions for the PAD model"

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
        str: An error response if a PAD value is less than 0 or greater than 100.
    """

    if len(emotional_entity) == 9:
        emotional_entity[6] += pleasure_amount
        emotional_entity[7] += activation_amount
        emotional_entity[8] += dominance_amount

        for i in range(6, 9):
            if emotional_entity[i] < 0:
                return "PAD values cannot be less than 0"
            elif emotional_entity[i] > 100:
                return "PAD values cannot be greater than 100"

    return emotional_entity
