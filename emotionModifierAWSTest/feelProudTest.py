import unittest
from .AWSLambdaConnection import feel_proud


class TestFeelProud(unittest.TestCase):
    ########## Paul Ekman's emotional model test ##########

    # Test to verify successful update of happiness and anger with a positive amount
    def test_successful_feel_proud_positive_amount(self):
        # Input values
        emotional_entity = [10, 0, 0, 0, 0, 0]
        happiness_amount = 30
        anger_amount = 10

        # Call updateHappiness function
        result = feel_proud(emotional_entity, happiness_amount, anger_amount)

        # Check that the result is not None
        self.assertIsNotNone(result)
        # Check that the result is of the expected type
        self.assertIsInstance(result, list)
        # Check if the result has the expected size
        self.assertEqual(len(result), 6)
        # Expected response
        self.assertEqual(result, [40, 0, 0, 10, 0, 0])

    # Test to verify successful update of happiness and anger with a negative amount
    def test_successful_feel_proud_negative_amount(self):
        emotional_entity = [50, 0, 0, 30, 0, 0]
        happiness_amount = -10
        anger_amount = -5

        result = feel_proud(emotional_entity, happiness_amount, anger_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [40, 0, 0, 25, 0, 0])

    # Test to verify update when emotional entity, happiness and anger amount are null
    def test_null(self):
        emotional_entity = [0, 0, 0, 0, 0, 0]
        happiness_amount = 0
        anger_amount = 0

        result = feel_proud(emotional_entity, happiness_amount, anger_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [0, 0, 0, 0, 0, 0])

    # Test to verify error when emotional entity contains non-integer values
    def test_error_non_integer_emotional_entity(self):
        emotional_entity = ["a", 10, 30, 40, 5, 5]
        happiness_amount = 10
        anger_amount = 10

        result = feel_proud(emotional_entity, happiness_amount, anger_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity contains negative values
    def test_error_negative_emotional_entity(self):
        emotional_entity = [-10, 10, 30, 5, 0, 6]
        happiness_amount = 10
        anger_amount = 10

        result = feel_proud(emotional_entity, happiness_amount, anger_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity is not a list
    def test_error_non_list_emotional_entity(self):
        emotional_entity = "10, 10, 30, 5, 0, 6"
        happiness_amount = 10
        anger_amount = 10

        result = feel_proud(emotional_entity, happiness_amount, anger_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity has incorrect number of positions
    def test_error_array_positions(self):
        emotional_entity = [0, 0, 0, 0]
        happiness_amount = 0
        anger_amount = 10

        result = feel_proud(emotional_entity, happiness_amount, anger_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotEqual(len(result), 6)
        self.assertEqual(
            result,
            "The list of emotions must have 6 positions for the Paul Ekman model or 9 positions for the PAD model",
        )

    # Test to verify error when happiness and anger amount is not an integer
    def test_error_non_integer_happiness_amount(self):
        emotional_entity = [50, 10, 0, 0, 0, 0]
        happiness_amount = "a"
        anger_amount = "10"

        result = feel_proud(emotional_entity, happiness_amount, anger_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    # Test to verify normalization of excessively negative happiness and anger amount
    def test_normalize_excessive_negative_happiness_amount(self):
        emotional_entity = [10, 10, 30, 5, 0, 6]
        happiness_amount = -15
        anger_amount = -10

        result = feel_proud(emotional_entity, happiness_amount, anger_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [0, 10, 30, 0, 0, 6])

    # Test to verify normalization of excessive emotional array
    def test_normalize_excessive_array(self):
        emotional_entity = [200, 10, 30, 40, 5, 5]
        happiness_amount = 10
        anger_amount = 10

        result = feel_proud(emotional_entity, happiness_amount, anger_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [67, 3, 9, 16, 1, 1])

    # Test to verify normalization of excessive happiness and anger amount
    def test_normalize_excessive_happiness_amount(self):
        emotional_entity = [10, 10, 30, 40, 5, 5]
        happiness_amount = 150
        anger_amount = 125

        result = feel_proud(emotional_entity, happiness_amount, anger_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [42, 2, 8, 44, 1, 1])

    # ########## PAD's emotional model test ##########

    # Test to verify successful update of happiness and anger with positive amount for PAD model
    def test_successful_feel_proud_positive_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        happiness_amount = 30
        anger_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [40, 10, 10, 15, 5, 12, 55, 90, 92])

    # Test to verify successful update of happiness and anger with negative amount for PAD model
    def test_successful_feel_proud_negative_amount_PAD(self):
        emotional_entity = [10, 10, 10, 25, 5, 12, 50, 60, 10]
        happiness_amount = -5
        anger_amount = -10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [5, 10, 10, 15, 5, 12, 55, 90, 92])

    # Test to verify update when all values and the emotional entity are null for PAD model
    def test_null_PAD(self):
        emotional_entity = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        happiness_amount = 0
        anger_amount = 0
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
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
        happiness_amount = 30
        anger_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
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
        happiness_amount = 10
        anger_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
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
        happiness_amount = 10
        anger_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
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
        happiness_amount = 0
        anger_amount = 0
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
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

    # Test to verify error due to non-integer happiness and anger amount in PAD model
    def test_error_non_integer_happiness_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        happiness_amount = [30, "a"]
        anger_amount = "10"
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
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
        happiness_amount = 8
        anger_amount = 10
        pleasure_amount = 5
        activation_amount = [30, "a"]
        dominance_amount = 82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    # Test to verify normalization of excessively negative happiness and anger amount in PAD model
    def test_normalize_excessive_negative_happiness_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        happiness_amount = -60
        anger_amount = -50
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [0, 10, 10, 0, 5, 12, 25, 90, 92])

    # Test to verify normalization of excessive emotional array for PAD model
    def test_normalize_excessive_array_PAD(self):
        emotional_entity = [10, 100, 10, 50, 87, 12, 50, 60, 10]
        happiness_amount = 10
        anger_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [6, 34, 3, 20, 30, 4, 55, 90, 92])

    # Test to verify normalization of excessive happiness and anger amount for PAD model
    def test_normalize_excessive_happiness_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        happiness_amount = 300
        anger_amount = 200
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [56, 1, 1, 37, 0, 2, 55, 90, 92])

    # Test to verify normalization of negative dominance amount in PAD model
    def test_normalize_negative_dominance_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        happiness_amount = 2
        anger_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = -82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [12, 10, 10, 15, 5, 12, 25, 90, 0])

    # Test to verify normalization of excessively high pleasure amount in PAD model
    def test_normalize_excessive_pleasure_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        happiness_amount = 30
        anger_amount = 10
        pleasure_amount = 500
        activation_amount = 30
        dominance_amount = 82

        result = feel_proud(
            emotional_entity,
            happiness_amount,
            anger_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [40, 10, 10, 15, 5, 12, 100, 90, 92])


if __name__ == "__main__":
    unittest.main()
