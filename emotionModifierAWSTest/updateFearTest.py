import unittest
from .AWSLambdaConnection import update_fear


class TestUpdateFear(unittest.TestCase):
    ########## Paul Ekman's emotional model test ##########

    # Test to verify successful update of fear with a positive amount
    def test_successful_update_fear_positive_amount(self):
        # Input values
        emotional_entity = [0, 0, 10, 0, 0, 0]
        fear_amount = 30

        # Call updatefear function
        result = update_fear(emotional_entity, fear_amount)

        # Check that the result is not None
        self.assertIsNotNone(result)
        # Check that the result is of the expected type
        self.assertIsInstance(result, list)
        # Check if the result has the expected size
        self.assertEqual(len(result), 6)
        # Expected response
        self.assertEqual(result, [0, 0, 40, 0, 0, 0])

    # Test to verify successful update of fear with a negative amount
    def test_successful_update_fear_negative_amount(self):
        emotional_entity = [0, 0, 50, 0, 0, 0]
        fear_amount = -10

        result = update_fear(emotional_entity, fear_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [0, 0, 40, 0, 0, 0])

    # Test to verify update when emotional entity and fear amount are both null
    def test_null(self):
        emotional_entity = [0, 0, 0, 0, 0, 0]
        fear_amount = 0

        result = update_fear(emotional_entity, fear_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [0, 0, 0, 0, 0, 0])

    # Test to verify error when emotional entity contains non-integer values
    def test_error_non_integer_emotional_entity(self):
        emotional_entity = ["a", 10, 30, 40, 5, 5]
        fear_amount = 10

        result = update_fear(emotional_entity, fear_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity contains negative values
    def test_error_negative_emotional_entity(self):
        emotional_entity = [-10, 10, 30, 5, 0, 6]
        fear_amount = 10

        result = update_fear(emotional_entity, fear_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity is not a list
    def test_error_non_list_emotional_entity(self):
        emotional_entity = "10, 10, 30, 5, 0, 6"
        fear_amount = 10

        result = update_fear(emotional_entity, fear_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity has incorrect number of positions
    def test_error_array_positions(self):
        emotional_entity = [0, 0, 0, 0]
        fear_amount = 0

        result = update_fear(emotional_entity, fear_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotEqual(len(result), 6)
        self.assertEqual(
            result,
            "The list of emotions must have 6 positions for the Paul Ekman model or 9 positions for the PAD model",
        )

    # Test to verify error when fear amount is not an integer
    def test_error_non_integer_fear_amount(self):
        emotional_entity = [50, 10, 0, 0, 0, 0]
        fear_amount = "a"

        result = update_fear(emotional_entity, fear_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    # Test to verify normalization of excessively negative fear amount
    def test_normalize_excessive_negative_fear_amount(self):
        emotional_entity = [10, 10, 30, 5, 0, 6]
        fear_amount = -15

        result = update_fear(emotional_entity, fear_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [10, 10, 15, 5, 0, 6])

    # Test to verify normalization of excessive emotional array
    def test_normalize_excessive_array(self):
        emotional_entity = [200, 10, 30, 40, 5, 5]
        fear_amount = 10

        result = update_fear(emotional_entity, fear_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [66, 3, 13, 13, 1, 1])

    # Test to verify normalization of excessive fear amount
    def test_normalize_excessive_fear_amount(self):
        emotional_entity = [10, 10, 30, 40, 5, 5]
        fear_amount = 150

        result = update_fear(emotional_entity, fear_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [4, 4, 72, 16, 2, 2])

    # ########## PAD's emotional model test ##########

    # Test to verify successful update of fear with positive amount for PAD model
    def test_successful_update_fear_positive_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        fear_amount = 30
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_fear(
            emotional_entity,
            fear_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 40, 5, 5, 12, 55, 90, 92])

    # Test to verify successful update of fear with negative amount for PAD model
    def test_successful_update_fear_negative_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        fear_amount = -5
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_fear(
            emotional_entity,
            fear_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 5, 5, 5, 12, 55, 90, 92])

    # Test to verify update when all values and the emotional entity are null for PAD model
    def test_null_PAD(self):
        emotional_entity = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        fear_amount = 0
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = update_fear(
            emotional_entity,
            fear_amount,
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
        fear_amount = 30
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_fear(
            emotional_entity,
            fear_amount,
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
        fear_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_fear(
            emotional_entity,
            fear_amount,
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
        fear_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_fear(
            emotional_entity,
            fear_amount,
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
        fear_amount = 0
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = update_fear(
            emotional_entity,
            fear_amount,
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

    # Test to verify error due to non-integer fear amount in PAD model
    def test_error_non_integer_fear_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        fear_amount = [30, "a"]
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_fear(
            emotional_entity,
            fear_amount,
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
        fear_amount = 8
        pleasure_amount = 5
        activation_amount = [30, "a"]
        dominance_amount = 82

        result = update_fear(
            emotional_entity,
            fear_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    # Test to verify normalization of excessively negative fear amount in PAD model
    def test_normalize_excessive_negative_fear_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        fear_amount = -60
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_fear(
            emotional_entity,
            fear_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 0, 5, 5, 12, 25, 90, 92])

    # Test to verify normalization of excessive emotional array for PAD model
    def test_normalize_excessive_array_PAD(self):
        emotional_entity = [10, 100, 10, 50, 87, 12, 50, 60, 10]
        fear_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_fear(
            emotional_entity,
            fear_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [3, 35, 7, 17, 31, 4, 55, 90, 92])

    # Test to verify normalization of excessive fear amount for PAD model
    def test_normalize_excessive_fear_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        fear_amount = 300
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_fear(
            emotional_entity,
            fear_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [2, 2, 88, 1, 1, 3, 55, 90, 92])

    # Test to verify normalization of negative dominance amount in PAD model
    def test_normalize_negative_dominance_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        fear_amount = 2
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = -82

        result = update_fear(
            emotional_entity,
            fear_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 12, 5, 5, 12, 25, 90, 0])

    # Test to verify normalization of excessively high pleasure amount in PAD model
    def test_normalize_excessive_pleasure_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        fear_amount = 30
        pleasure_amount = 500
        activation_amount = 30
        dominance_amount = 82

        result = update_fear(
            emotional_entity,
            fear_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 40, 5, 5, 12, 100, 90, 92])


if __name__ == "__main__":
    unittest.main()
