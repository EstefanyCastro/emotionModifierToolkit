from updateEmotions import update_emotions


def update_happiness(emotional_entity, happiness_amount):
    """
    Increases or decrease the happiness emotion in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        happiness_amount (int): The amount of happiness mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, happiness_amount, 0, 0, 0, 0, 0)


def update_sadness(emotional_entity, sadness_amount):
    """
    Increases or decrease the sadness emotion in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        sadness_amount (int): The amount of sadness mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, sadness_amount, 0, 0, 0, 0)


def update_fear(emotional_entity, fear_amount):
    """
    Increases or decrease the fear emotion in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        fear_amount (int): The amount of fear mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, 0, fear_amount, 0, 0, 0)


def update_anger(emotional_entity, anger_amount):
    """
    Increases or decrease the anger emotion in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        anger_amount (int): The amount of anger mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, 0, 0, anger_amount, 0, 0)


def update_disgust(emotional_entity, disgust_amount):
    """
    Increases or decrease the disgust emotion in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        disgust_amount (int): The amount of disgust mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, 0, 0, 0, disgust_amount, 0)


def update_surprise(emotional_entity, surprise_amount):
    """
    Increases or decrease the surprise emotion in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, 0, 0, 0, 0, surprise_amount)


def update_positive_emotions(emotional_entity, happiness_amount, surprise_amount):
    """
    Mutate the emotions of happiness and surprise in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        happiness_amount (int): The amount of happiness mutation.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(
        emotional_entity, happiness_amount, 0, 0, 0, 0, surprise_amount
    )


def update_negative_emotions(
    emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
):
    """
    Mutate the emotions of sadness, fear, anger and disgust in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        sadness_amount (int): The amount of sadness mutation.
        fear_amount (int): The amount of fear mutation.
        anger_amount (int): The amount of anger mutation.
        disgust_amount (int): The amount of disgust mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(
        emotional_entity,
        0,
        sadness_amount,
        fear_amount,
        anger_amount,
        disgust_amount,
        0,
    )


def update_feel_shame(emotional_entity, fear_amount, disgust_amount):
    """
    Mutate the emotions of fear and disgust in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        fear_amount (int): The amount of fear mutation.
        disgust_amount (int): The amount of disgust mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, 0, fear_amount, 0, disgust_amount, 0)


def update_feel_proud(emotional_entity, happiness_amount, anger_amount):
    """
    Mutate the emotions of happiness and anger in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        happiness_amount (int): The amount of happiness mutation.
        anger_amount (int): The amount of anger mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, happiness_amount, 0, 0, anger_amount, 0, 0)


def update_feel_jealous(emotional_entity, sadness_amount, anger_amount):
    """
    Mutate the emotions of sadness and anger in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        sadness_amount (int): The amount of sadness mutation.
        anger_amount (int): The amount of anger mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, sadness_amount, 0, anger_amount, 0, 0)


def update_feel_indignation(emotional_entity, anger_amount, surprise_amount):
    """
    Mutate the emotions of anger and surprise in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        anger_amount (int): The amount of anger mutation.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, 0, 0, anger_amount, 0, surprise_amount)


def update_feel_indiference(emotional_entity, anger_amount, disgust_amount):
    """
    Mutate the emotions of anger and disgust in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        anger_amount (int): The amount of anger mutation.
        disgust_amount (int): The amount of disgust mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, 0, 0, anger_amount, disgust_amount, 0)


def update_feel_guilty(emotional_entity, happiness_amount, fear_amount):
    """
    Mutate the emotions of happiness and fear in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        happiness_amount (int): The amount of happiness mutation.
        fear_amount (int): The amount of fear mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, happiness_amount, 0, fear_amount, 0, 0, 0)


def update_feel_envy(emotional_entity, sadness_amount, anger_amount):
    """
    Mutate the emotions of sadness and anger in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        sadness_amount (int): The amount of sadness mutation.
        anger_amount (int): The amount of anger mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, sadness_amount, 0, anger_amount, 0, 0)


def update_feel_disappointment(emotional_entity, sadness_amount, surprise_amount):
    """
    Mutate the emotions of sadness and surprise in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        sadness_amount (int): The amount of sadness mutation.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(
        emotional_entity, 0, sadness_amount, 0, 0, 0, surprise_amount
    )


def update_feel_despair(emotional_entity, sadness_amount, fear_amount):
    """
    Mutate the emotions of sadness and fear in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        sadness_amount (int): The amount of sadness mutation.
        fear_amount (int): The amount of fear mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, sadness_amount, fear_amount, 0, 0, 0)


def update_feel_delight(emotional_entity, happiness_amount, surprise_amount):
    """
    Mutate the emotions of happiness and surprise in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        happiness_amount (int): The amount of happiness mutation.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(
        emotional_entity, happiness_amount, 0, 0, 0, 0, surprise_amount
    )


def update_feel_alarm(emotional_entity, fear_amount, surprise_amount):
    """
    Mutate the emotions of fear and surprise in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        fear_amount (int): The amount of fear mutation.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(emotional_entity, 0, 0, fear_amount, 0, 0, surprise_amount)


def update_experience_natural_disaster(
    emotional_entity, sadness_amount, fear_amount, surprise_amount
):
    """
    Mutate the emotions of sadness, fear and surprise in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        sadness_amount (int): The amount of sadness mutation.
        fear_amount (int): The amount of fear mutation.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(
        emotional_entity, 0, sadness_amount, fear_amount, 0, 0, surprise_amount
    )


def update_experience_injustice(
    emotional_entity, sadness_amount, fear_amount, anger_amount, surprise_amount
):
    """
    Mutate the emotions of sadness, fear, anger and surprise in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        sadness_amount (int): The amount of sadness mutation.
        fear_amount (int): The amount of fear mutation.
        anger_amount (int): The amount of anger mutation.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(
        emotional_entity,
        0,
        sadness_amount,
        fear_amount,
        anger_amount,
        0,
        surprise_amount,
    )


def update_experience_crowd(
    emotional_entity, fear_amount, anger_amount, surprise_amount
):
    """
    Mutate the emotions of fear, anger and surprise in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        fear_amount (int): The amount of fear mutation.
        anger_amount (int): The amount of anger mutation.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(
        emotional_entity, 0, 0, fear_amount, anger_amount, 0, surprise_amount
    )


def update_exciting_experience(emotional_entity, happiness_amount, surprise_amount):
    """
    Mutate the emotions of happiness and surprise in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        happiness_amount (int): The amount of happiness mutation.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(
        emotional_entity, happiness_amount, 0, 0, 0, 0, surprise_amount
    )


def update_be_criticized(
    emotional_entity, sadness_amount, anger_amount, surprise_amount
):
    """
    Mutate the emotions of sadness, anger and surprise in the emotional entity.

    Args:
        emotional_entity (list): The list of emotional values.
        sadness_amount (int): The amount of sadness mutation.
        anger_amount (int): The amount of anger mutation.
        surprise_amount (int): The amount of surprise mutation.

    Returns:
        list: The updated emotional entity.
        str: Returns an error message.
    """
    return update_emotions(
        emotional_entity, 0, sadness_amount, 0, anger_amount, 0, surprise_amount
    )
