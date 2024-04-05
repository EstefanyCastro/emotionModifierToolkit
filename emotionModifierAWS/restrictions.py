def validate_emotional_entity(emotional_entity):
    # Validates the emotional entity list, ensuring it's a list of positive integers or zero.

    if not isinstance(emotional_entity, list) or any(
        not isinstance(x, int) or x < 0 for x in emotional_entity
    ):
        return "The list of emotions must contain only positive integers or zero"
    return None


def validate_emotional_entity_length(emotional_entity):
    # Validates the length of the emotional entity list.

    if len(emotional_entity) not in [6, 9]:
        return "The list of emotions must have 6 positions for the Paul Ekman model or 9 positions for the PAD model"
    return None


def validate_amounts(
    pleasure_amount,
    activation_amount,
    dominance_amount,
    happiness_amount,
    sadness_amount,
    fear_amount,
    anger_amount,
    disgust_amount,
    surprise_amount,
):
    # Validates all amounts, ensuring they are integers.

    if not all(
        isinstance(value, int)
        for value in [
            pleasure_amount,
            activation_amount,
            dominance_amount,
            happiness_amount,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            surprise_amount,
        ]
    ):
        return "All amounts must be integers"
    return None


def validate_emotions(emotions):
    # Validates emotional values.

    for i in emotions:
        if i < 0:
            return "Emotions cannot be negative"
    total_emotions_sum = sum(emotions)
    if total_emotions_sum > 100:
        return "The total sum of emotions cannot exceed 100"
    return None


def validate_pad_values(pad_values):
    # Validates PAD values.

    for i in pad_values:
        if i < 0 or i > 100:
            return "PAD values cannot be less than 0 or greater than 100"
    return None
