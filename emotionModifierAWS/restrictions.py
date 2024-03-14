def validate_emotional_entity(emotional_entity):
    # Validates the emotional entity list, ensuring it's a list of positive integers or zero.

    if (
        not isinstance(emotional_entity, list)
        or not all(isinstance(x, int) for x in emotional_entity)
        or any(x < 0 for x in emotional_entity)
    ):
        return "The list of emotions must contain only positive integers or zero"

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
        isinstance(x, int)
        for x in [
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
        return "The amount of emotions and the amount of PAD values must be integers"

    return None
