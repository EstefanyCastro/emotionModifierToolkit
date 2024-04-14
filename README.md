# Development of a toolkit for the application of Paul Ekman's and James A. Russell's emotional models in academic work on affective computing.

This project provides a set of tools aimed at facilitating the analysis and manipulation of emotional entities using Paul Ekman's and James A. Russell's PAD models. It provides specialized functions to validate, normalize and update these emotional entities, thus enabling a more accurate and complete emotional analysis.

## Usage:

The toolkit consists of several functions designed to address different aspects of emotional entity processing. The main functions are detailed below:

### Validation of Emotional Entities:

- `validate_emotional_entity(emotional_entity)`: Checks that a list of emotional entities contains only positive integers or zero.
- `validate_emotional_entity_length(emotional_entity)`: Ensures that the list of emotional entities has the appropriate length, i.e., 6 positions for the Paul Ekman model and 9 positions for the PAD model integration.
- `validate_amounts(pleasure_amount, activation_amount, dominance_amount, **kargs_amount)`: Validates that all amounts are integers.

### Emotions and PAD Normalization:

- `normalize_emotions(emotions)`: Adjusts a list of emotions to be within the range [0, 100].
- `normalize_pad_values(pad_values)`: Normalizes PAD values to be within the range [0, 100].

### Update Emotional Entities:

- `update_*function(emotional_entity, **kargs_amount)`: Increases or decreases the specified emotion(s) in the emotional entity.
- `update_pad_values(emotional_entity, pleasure_amount, activation_amount, dominance_amount)`: Updates PAD values in the emotional entity.

### Lambda Handler:

- `lambda_handler(event, context)`: Lambda function in charge of handling emotional entity updates. It receives JSON events containing information about the emotional entity and amounts changes, and returns a JSON response including the HTTP status code and the updated emotional entity.
