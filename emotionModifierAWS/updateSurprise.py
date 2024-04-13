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
    pleasure_amount, activation_amount, dominance_amount, surprise_amount
):
    # Validates all amounts, ensuring they are integers.

    if not all(
        isinstance(x, int)
        for x in [
            pleasure_amount,
            activation_amount,
            dominance_amount,
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
    return None


def normalize_emotions(emotions):
    # If the sum of the emotions is greater than 100, we normalize the list of emotions.
    total_emotions_sum = sum(emotions)

    if total_emotions_sum > 100:
        normalized_emotions = [
            int(emotion * 100 / total_emotions_sum) for emotion in emotions
        ]
        return normalized_emotions
    else:
        return emotions


def validate_pad_values(pad_values):
    # Validates PAD values.

    for i in pad_values:
        if i < 0:
            return "PAD values cannot be less than 0"
    return None


def normalize_pad_values(pad_values):
    # Normalize the PAD values to ensure that they do not exceed the range of 100.

    normalized_values = [min(value, 100) for value in pad_values]
    return normalized_values


def update_surprise(emotional_entity, surprise_amount):
    """
    Increases or decrease the surprise emotion in the emotional entity.
    """
    error_length = validate_emotional_entity_length(emotional_entity)
    if error_length:
        return error_length

    if len(emotional_entity) == 6 or len(emotional_entity) == 9:
        emotional_entity[5] += surprise_amount

        error = validate_emotions(emotional_entity[:6])
        if error:
            return error

        emotional_entity[:6] = normalize_emotions(emotional_entity[:6])

    return emotional_entity


def update_pad_values(
    emotional_entity, pleasure_amount, activation_amount, dominance_amount
):
    """
    Updates the PAD values in the emotional entity.
    """

    if len(emotional_entity) == 9:
        emotional_entity[6] += pleasure_amount
        emotional_entity[7] += activation_amount
        emotional_entity[8] += dominance_amount

        error = validate_pad_values(emotional_entity[6:])
        if error:
            return error

        emotional_entity[6:] = normalize_pad_values(emotional_entity[6:])

    return emotional_entity


def lambda_handler(event, context):
    """
    Lambda function to handle emotional entity updates.

    Args:
        event (json): The event containing emotional entity and mutation amounts.
            - emotional_entity (list): The list of emotional values.
            - surprise_amount (int): The amount of surprise mutation.
            - pleasure_amount (int): The amount of pleasure mutation.
            - activation_amount (int): The amount of activation mutation.
            - dominance_amount (int): The amount of dominance mutation.
        context: None

    Returns:
        json: A dictionary containing the HTTP status code and the updated emotional entity.
            - statusCode (int): The HTTP status code.
                - 200: Success.
                - 400: Bad request.
            - body (list or str): The updated emotional entity or an error message.
    """

    # Gets the event parameters
    emotional_entity = event.get("emotional_entity", [])
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
        pleasure_amount, activation_amount, dominance_amount, surprise_amount
    )
    if validation_error:
        return {"statusCode": 400, "body": validation_error}

    # Upgrades surprise
    updated_emotional_entity = update_surprise(emotional_entity, surprise_amount)
    if isinstance(updated_emotional_entity, str):
        return {"statusCode": 400, "body": updated_emotional_entity}

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
