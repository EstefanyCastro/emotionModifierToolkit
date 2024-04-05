from updateEmotions import update_emotions


def update_happiness(emotional_entity, happiness_amount):
    return update_emotions(emotional_entity, happiness_amount, 0, 0, 0, 0, 0)


def update_sadness(emotional_entity, sadness_amount):
    return update_emotions(emotional_entity, 0, sadness_amount, 0, 0, 0, 0)


def update_fear(emotional_entity, fear_amount):
    return update_emotions(emotional_entity, 0, 0, fear_amount, 0, 0, 0)


def update_anger(emotional_entity, anger_amount):
    return update_emotions(emotional_entity, 0, 0, 0, anger_amount, 0, 0)


def update_disgust(emotional_entity, disgust_amount):
    return update_emotions(emotional_entity, 0, 0, 0, 0, disgust_amount, 0)


def update_surprise(emotional_entity, surprise_amount):
    return update_emotions(emotional_entity, 0, 0, 0, 0, 0, surprise_amount)


def update_positive_emotions(emotional_entity, happiness_amount, surprise_amount):
    return update_emotions(
        emotional_entity, happiness_amount, 0, 0, 0, 0, surprise_amount
    )


def update_negative_emotions(
    emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
):
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
    return update_emotions(emotional_entity, 0, 0, fear_amount, 0, disgust_amount, 0)


def update_feel_proud(emotional_entity, happiness_amount, anger_amount):
    return update_emotions(emotional_entity, happiness_amount, 0, 0, anger_amount, 0, 0)


def update_feel_jealous(emotional_entity, sadness_amount, anger_amount):
    return update_emotions(emotional_entity, 0, sadness_amount, 0, anger_amount, 0, 0)


def update_feel_indignation(emotional_entity, anger_amount, surprise_amount):
    return update_emotions(emotional_entity, 0, 0, 0, anger_amount, 0, surprise_amount)


def update_feel_indiference(emotional_entity, anger_amount, disgust_amount):
    return update_emotions(emotional_entity, 0, 0, 0, anger_amount, disgust_amount, 0)


def update_feel_guilty(emotional_entity, happiness_amount, fear_amount):
    return update_emotions(emotional_entity, happiness_amount, 0, fear_amount, 0, 0, 0)


def update_feel_envy(emotional_entity, sadness_amount, anger_amount):
    return update_emotions(emotional_entity, 0, sadness_amount, 0, anger_amount, 0, 0)


def update_feel_disappointment(emotional_entity, sadness_amount, surprise_amount):
    return update_emotions(
        emotional_entity, 0, sadness_amount, 0, 0, 0, surprise_amount
    )


def update_feel_despair(emotional_entity, sadness_amount, fear_amount):
    return update_emotions(emotional_entity, 0, sadness_amount, fear_amount, 0, 0, 0)


def update_feel_delight(emotional_entity, happiness_amount, surprise_amount):
    return update_emotions(
        emotional_entity, happiness_amount, 0, 0, 0, 0, surprise_amount
    )


def update_feel_alarm(emotional_entity, fear_amount, surprise_amount):
    return update_emotions(emotional_entity, 0, 0, fear_amount, 0, 0, surprise_amount)


def update_experience_natural_disaster(
    emotional_entity, sadness_amount, fear_amount, surprise_amount
):
    return update_emotions(
        emotional_entity, 0, sadness_amount, fear_amount, 0, 0, surprise_amount
    )


def update_experience_injustice(
    emotional_entity, sadness_amount, fear_amount, anger_amount, surprise_amount
):
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
    return update_emotions(
        emotional_entity, 0, 0, fear_amount, anger_amount, 0, surprise_amount
    )


def update_exciting_experience(emotional_entity, happiness_amount, surprise_amount):
    return update_emotions(
        emotional_entity, happiness_amount, 0, 0, 0, 0, surprise_amount
    )


def update_be_criticized(
    emotional_entity, sadness_amount, anger_amount, surprise_amount
):
    return update_emotions(
        emotional_entity, 0, sadness_amount, 0, anger_amount, 0, surprise_amount
    )
