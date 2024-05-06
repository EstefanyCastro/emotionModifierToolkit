import unittest
from .AWSLambdaConnection import update_negative_emotions


class TestUpdateNegativeEmotions(unittest.TestCase):
    ########## Paul Ekman's emotional model test ##########

    # Test to verify successful update of sadness, fear, anger and disgust with a positive amount
    def test_successful_update_negative_emotions_positive_amount(self):
        # Input values
        emotional_entity = [0, 0, 0, 0, 0, 0]
        sadness_amount = 30
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5

        # Call updatesadness function
        result = update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        )

        # Check that the result is not None
        self.assertIsNotNone(result)
        # Check that the result is of the expected type
        self.assertIsInstance(result, list)
        # Check if the result has the expected size
        self.assertEqual(len(result), 6)
        # Expected response
        self.assertEqual(result, [0, 30, 20, 10, 5, 0])

    # Test to verify successful update of sadness, fear, anger and disgust with a negative amount
    def test_successful_update_negative_emotions_negative_amount(self):
        emotional_entity = [0, 20, 40, 40, 45, 0]
        sadness_amount = -10
        fear_amount = -20
        anger_amount = -10
        disgust_amount = -5

        result = update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [0, 10, 20, 30, 40, 0])

    # Test to verify update when emotional entity, sadness, fear, anger and disgust amount are null
    def test_null(self):
        emotional_entity = [0, 0, 0, 0, 0, 0]
        sadness_amount = 0
        fear_amount = 0
        anger_amount = 0
        disgust_amount = 0

        result = update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [0, 0, 0, 0, 0, 0])

    # Test to verify error when emotional entity contains non-integer values
    def test_error_non_integer_emotional_entity(self):
        emotional_entity = ["a", 10, 30, 40, 5, 5]
        sadness_amount = 10
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5

        result = update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity contains negative values
    def test_error_negative_emotional_entity(self):
        emotional_entity = [-10, 10, 30, 5, 0, 6]
        sadness_amount = 10
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5

        result = update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity is not a list
    def test_error_non_list_emotional_entity(self):
        emotional_entity = "10, 10, 30, 5, 0, 6"
        sadness_amount = 10
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5

        result = update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity has incorrect number of positions
    def test_error_array_positions(self):
        emotional_entity = [0, 0, 0, 0]
        sadness_amount = 0
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5

        result = update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotEqual(len(result), 6)
        self.assertEqual(
            result,
            "The list of emotions must have 6 positions for the Paul Ekman model or 9 positions for the PAD model",
        )

    # Test to verify error when sadness, fear, anger or disgust amount is not an integer
    def test_error_non_integer_sadness_amount(self):
        emotional_entity = [50, 10, 0, 0, 0, 0]
        sadness_amount = "a"
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5

        result = update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    # Test to verify normalization of excessively negative sadness, fear, anger or disgust amount
    def test_normalize_excessive_negative_sadness_amount(self):
        emotional_entity = [10, 20, 30, 5, 0, 6]
        sadness_amount = -10
        fear_amount = 20
        anger_amount = 10
        disgust_amount = -5

        result = update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [10, 10, 50, 15, 0, 6])

    # Test to verify normalization of excessive emotional array
    def test_normalize_excessive_array(self):
        emotional_entity = [200, 10, 30, 40, 5, 5]
        sadness_amount = 10
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5

        result = update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [59, 5, 14, 14, 2, 1])

    # Test to verify normalization of excessive sadness, fear, anger or disgust amount
    def test_normalize_excessive_sadness_amount(self):
        emotional_entity = [10, 10, 30, 40, 5, 5]
        sadness_amount = 150
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 500

        result = update_negative_emotions(
            emotional_entity, sadness_amount, fear_amount, anger_amount, disgust_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [1, 20, 6, 6, 64, 0])

    # ########## PAD's emotional model test ##########

    # Test to verify successful update of sadness, fear, anger and disgust with positive amount for PAD model
    def test_successful_update_negative_emotions_positive_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        sadness_amount = 3
        fear_amount = 5
        anger_amount = 2
        disgust_amount = 5
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 13, 15, 7, 10, 12, 55, 90, 92])

    # Test to verify successful update of sadness, fear, anger and disgust with negative amount for PAD model
    def test_successful_update_negative_emotions_negative_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        sadness_amount = -5
        fear_amount = 20
        anger_amount = -2
        disgust_amount = 5
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 5, 30, 3, 10, 12, 55, 90, 92])

    # Test to verify update when all values and the emotional entity are null for PAD model
    def test_null_PAD(self):
        emotional_entity = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        sadness_amount = 0
        fear_amount = 0
        anger_amount = 0
        disgust_amount = 0
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [0, 0, 0, 0, 0, 0, 0, 0, 0])

    # Test to verify error due to non-integer emotional array for PAD model
    def test_error_non_integer_emotional_entity_PAD(self):
        emotional_entity = [10, 10, "10", 5, 5, 12, 50, 60, 10]
        sadness_amount = 30
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error due to negative values in emotional array for PAD model
    def test_error_negative_emotional_entity_PAD(self):
        emotional_entity = [-10, 10, 10, 5, 5, 12, 20, 60, 10]
        sadness_amount = 10
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity is not a list for PAD model
    def test_error_non_list_emotional_entity_PAD(self):
        emotional_entity = "10, 10, 10, 5, 5, 12, 20, 60, 10"
        sadness_amount = 10
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error due to incorrect number of positions in emotional array for PAD model
    def test_error_array_positions_PAD(self):
        emotional_entity = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sadness_amount = 0
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotEqual(len(result), 9)
        self.assertEqual(
            result,
            "The list of emotions must have 6 positions for the Paul Ekman model or 9 positions for the PAD model",
        )

    # Test to verify error due to non-integer sadness, fear, anger or disgust amount in PAD model
    def test_error_non_integer_sadness_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        sadness_amount = [30, "a"]
        fear_amount = 20
        anger_amount = 10
        disgust_amount = "5"
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    # Test to verify error due to non-integer activation amount in PAD model
    def test_error_non_integer_activation_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        sadness_amount = 8
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5
        pleasure_amount = 5
        activation_amount = [30, "a"]
        dominance_amount = 82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    # Test to verify normalization of excessively negative sadness, fear, anger or disgust amount in PAD model
    def test_normalize_excessive_negative_sadness_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        sadness_amount = -60
        fear_amount = -20
        anger_amount = -10
        disgust_amount = -5
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 0, 0, 0, 0, 12, 25, 90, 92])

    # Test to verify normalization of excessive emotional array for PAD model
    def test_normalize_excessive_array_PAD(self):
        emotional_entity = [10, 100, 10, 50, 87, 12, 50, 60, 10]
        sadness_amount = 10
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [3, 35, 9, 19, 29, 3, 55, 90, 92])

    # Test to verify normalization of excessive sadness, fear, anger or disgust amount for PAD model
    def test_normalize_excessive_sadness_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        sadness_amount = 300
        fear_amount = 20
        anger_amount = 100
        disgust_amount = 5
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [2, 64, 6, 22, 2, 2, 55, 90, 92])

    # Test to verify normalization of negative dominance amount in PAD model
    def test_normalize_negative_dominance_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        sadness_amount = 2
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 5
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = -82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 12, 30, 15, 10, 12, 25, 90, 0])

    # Test to verify normalization of excessively high pleasure amount in PAD model
    def test_normalize_excessive_pleasure_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        sadness_amount = 5
        fear_amount = 20
        anger_amount = 10
        disgust_amount = 0
        pleasure_amount = 500
        activation_amount = 30
        dominance_amount = 82

        result = update_negative_emotions(
            emotional_entity,
            sadness_amount,
            fear_amount,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 15, 30, 15, 5, 12, 100, 90, 92])


if __name__ == "__main__":
    unittest.main()
