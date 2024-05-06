import unittest
from .AWSLambdaConnection import feel_indifference


class TestFeelIndifference(unittest.TestCase):
    ########## Paul Ekman's emotional model test ##########

    # Test to verify successful update of anger and disgust with a positive amount
    def test_successful_feel_indifference_positive_amount(self):
        # Input values
        emotional_entity = [0, 0, 0, 10, 0, 0]
        anger_amount = 30
        disgust_amount = 10

        # Call updateHappiness function
        result = feel_indifference(emotional_entity, anger_amount, disgust_amount)

        # Check that the result is not None
        self.assertIsNotNone(result)
        # Check that the result is of the expected type
        self.assertIsInstance(result, list)
        # Check if the result has the expected size
        self.assertEqual(len(result), 6)
        # Expected response
        self.assertEqual(result, [0, 0, 0, 40, 10, 0])

    # Test to verify successful update of anger and disgust with a negative amount
    def test_successful_feel_indifference_negative_amount(self):
        emotional_entity = [0, 0, 0, 50, 30, 0]
        anger_amount = -10
        disgust_amount = -5

        result = feel_indifference(emotional_entity, anger_amount, disgust_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [0, 0, 0, 40, 25, 0])

    # Test to verify update when emotional entity, anger and disgust amount are null
    def test_null(self):
        emotional_entity = [0, 0, 0, 0, 0, 0]
        anger_amount = 0
        disgust_amount = 0

        result = feel_indifference(emotional_entity, anger_amount, disgust_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [0, 0, 0, 0, 0, 0])

    # Test to verify error when emotional entity contains non-integer values
    def test_error_non_integer_emotional_entity(self):
        emotional_entity = ["a", 10, 30, 40, 5, 5]
        anger_amount = 10
        disgust_amount = 10

        result = feel_indifference(emotional_entity, anger_amount, disgust_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity contains negative values
    def test_error_negative_emotional_entity(self):
        emotional_entity = [-10, 10, 30, 5, 0, 6]
        anger_amount = 10
        disgust_amount = 10

        result = feel_indifference(emotional_entity, anger_amount, disgust_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity is not a list
    def test_error_non_list_emotional_entity(self):
        emotional_entity = "10, 10, 30, 5, 0, 6"
        anger_amount = 10
        disgust_amount = 10

        result = feel_indifference(emotional_entity, anger_amount, disgust_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity has incorrect number of positions
    def test_error_array_positions(self):
        emotional_entity = [0, 0, 0, 0]
        anger_amount = 0
        disgust_amount = 10

        result = feel_indifference(emotional_entity, anger_amount, disgust_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotEqual(len(result), 6)
        self.assertEqual(
            result,
            "The list of emotions must have 6 positions for the Paul Ekman model or 9 positions for the PAD model",
        )

    # Test to verify error when anger and disgust amount is not an integer
    def test_error_non_integer_anger_amount(self):
        emotional_entity = [50, 10, 0, 0, 0, 0]
        anger_amount = "a"
        disgust_amount = "10"

        result = feel_indifference(emotional_entity, anger_amount, disgust_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    # Test to verify normalization of excessively negative anger and disgust amount
    def test_normalize_excessive_negative_anger_amount(self):
        emotional_entity = [10, 10, 30, 5, 0, 6]
        anger_amount = -15
        disgust_amount = -10

        result = feel_indifference(emotional_entity, anger_amount, disgust_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [10, 10, 30, 0, 0, 6])

    # Test to verify normalization of excessive emotional array
    def test_normalize_excessive_array(self):
        emotional_entity = [200, 10, 30, 40, 5, 5]
        anger_amount = 10
        disgust_amount = 10

        result = feel_indifference(emotional_entity, anger_amount, disgust_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [64, 3, 9, 16, 4, 1])

    # Test to verify normalization of excessive anger and disgust amount
    def test_normalize_excessive_anger_amount(self):
        emotional_entity = [10, 10, 30, 40, 5, 5]
        anger_amount = 150
        disgust_amount = 125

        result = feel_indifference(emotional_entity, anger_amount, disgust_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [2, 2, 8, 50, 34, 1])

    # ########## PAD's emotional model test ##########

    # Test to verify successful update of anger and disgust with positive amount for PAD model
    def test_successful_feel_indifference_positive_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        anger_amount = 30
        disgust_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_indifference(
            emotional_entity,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 10, 35, 15, 12, 55, 90, 92])

    # Test to verify successful update of anger and disgust with negative amount for PAD model
    def test_successful_feel_indifference_negative_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 25, 12, 50, 60, 10]
        anger_amount = -5
        disgust_amount = -10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_indifference(
            emotional_entity,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 10, 0, 15, 12, 55, 90, 92])

    # Test to verify update when all values and the emotional entity are null for PAD model
    def test_null_PAD(self):
        emotional_entity = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        anger_amount = 0
        disgust_amount = 0
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = feel_indifference(
            emotional_entity,
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
        anger_amount = 30
        disgust_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_indifference(
            emotional_entity,
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
        anger_amount = 10
        disgust_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_indifference(
            emotional_entity,
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
        anger_amount = 10
        disgust_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_indifference(
            emotional_entity,
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
        anger_amount = 0
        disgust_amount = 0
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = feel_indifference(
            emotional_entity,
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

    # Test to verify error due to non-integer anger and disgust amount in PAD model
    def test_error_non_integer_anger_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        anger_amount = [30, "a"]
        disgust_amount = "10"
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_indifference(
            emotional_entity,
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
        anger_amount = 8
        disgust_amount = 10
        pleasure_amount = 5
        activation_amount = [30, "a"]
        dominance_amount = 82

        result = feel_indifference(
            emotional_entity,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    # Test to verify normalization of excessively negative anger and disgust amount in PAD model
    def test_normalize_excessive_negative_anger_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        anger_amount = -60
        disgust_amount = -50
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_indifference(
            emotional_entity,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 10, 0, 0, 12, 25, 90, 92])

    # Test to verify normalization of excessive emotional array for PAD model
    def test_normalize_excessive_array_PAD(self):
        emotional_entity = [10, 100, 10, 50, 87, 12, 50, 60, 10]
        anger_amount = 10
        disgust_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_indifference(
            emotional_entity,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [3, 34, 3, 20, 33, 4, 55, 90, 92])

    # Test to verify normalization of excessive anger and disgust amount for PAD model
    def test_normalize_excessive_anger_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        anger_amount = 300
        disgust_amount = 200
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_indifference(
            emotional_entity,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [1, 1, 1, 55, 37, 2, 55, 90, 92])

    # Test to verify normalization of negative dominance amount in PAD model
    def test_normalize_negative_dominance_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        anger_amount = 2
        disgust_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = -82

        result = feel_indifference(
            emotional_entity,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 10, 7, 15, 12, 25, 90, 0])

    # Test to verify normalization of excessively high pleasure amount in PAD model
    def test_normalize_excessive_pleasure_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        anger_amount = 30
        disgust_amount = 10
        pleasure_amount = 500
        activation_amount = 30
        dominance_amount = 82

        result = feel_indifference(
            emotional_entity,
            anger_amount,
            disgust_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 10, 35, 15, 12, 100, 90, 92])


if __name__ == "__main__":
    unittest.main()
