import unittest
from .AWSLambdaConnection import experience_crowd


class TestExperienceCrowd(unittest.TestCase):
    ########## Paul Ekman's emotional model test ##########

    # Test to verify successful update of fear, anger and surprise with a positive amount
    def test_successful_experience_crowd_positive_amount(self):
        # Input values
        emotional_entity = [0, 0, 0, 0, 0, 0]
        fear_amount = 30
        anger_amount = 15
        surprise_amount = 10

        # Call updateHappiness function
        result = experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        )

        # Check that the result is not None
        self.assertIsNotNone(result)
        # Check that the result is of the expected type
        self.assertIsInstance(result, list)
        # Check if the result has the expected size
        self.assertEqual(len(result), 6)
        # Expected response
        self.assertEqual(result, [0, 0, 30, 15, 0, 10])

    # Test to verify successful update of fear, anger and surprise with a negative amount
    def test_successful_experience_crowd_negative_amount(self):
        emotional_entity = [0, 15, 30, 22, 0, 10]
        fear_amount = -10
        anger_amount = -15
        surprise_amount = -5

        result = experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [0, 15, 20, 7, 0, 5])

    # Test to verify update when emotional entity, fear, anger and surprise amount are null
    def test_null(self):
        emotional_entity = [0, 0, 0, 0, 0, 0]
        fear_amount = 0
        anger_amount = 0
        surprise_amount = 0

        result = experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [0, 0, 0, 0, 0, 0])

    # Test to verify error when emotional entity contains non-integer values
    def test_error_non_integer_emotional_entity(self):
        emotional_entity = ["a", 10, 30, 40, 5, 5]
        fear_amount = 10
        anger_amount = 15
        surprise_amount = 10

        result = experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity contains negative values
    def test_error_negative_emotional_entity(self):
        emotional_entity = [-10, 10, 30, 5, 0, 6]
        fear_amount = 10
        anger_amount = 15
        surprise_amount = 10

        result = experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity is not a list
    def test_error_non_list_emotional_entity(self):
        emotional_entity = "10, 10, 30, 5, 0, 6"
        fear_amount = 10
        anger_amount = 15
        surprise_amount = 10

        result = experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    # Test to verify error when emotional entity has incorrect number of positions
    def test_error_array_positions(self):
        emotional_entity = [0, 0, 0, 0]
        fear_amount = 0
        anger_amount = 15
        surprise_amount = 10

        result = experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotEqual(len(result), 6)
        self.assertEqual(
            result,
            "The list of emotions must have 6 positions for the Paul Ekman model or 9 positions for the PAD model",
        )

    # Test to verify error when fear, anger and surprise amount is not an integer
    def test_error_non_integer_fear_amount(self):
        emotional_entity = [50, 10, 0, 0, 0, 0]
        fear_amount = "a"
        anger_amount = 15
        surprise_amount = "10"

        result = experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    # Test to verify normalization of excessively negative fear, anger and surprise amount
    def test_normalize_excessive_negative_fear_amount(self):
        emotional_entity = [10, 10, 30, 5, 2, 6]
        fear_amount = -58
        anger_amount = -15
        surprise_amount = -10

        result = experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [10, 10, 0, 0, 2, 0])

    # Test to verify normalization of excessive emotional array
    def test_normalize_excessive_array(self):
        emotional_entity = [30, 10, 200, 425, 5, 5]
        fear_amount = 10
        anger_amount = 15
        surprise_amount = 10

        result = experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [4, 1, 29, 61, 0, 2])

    # Test to verify normalization of excessive fear, anger and surprise amount
    def test_normalize_excessive_fear_amount(self):
        emotional_entity = [10, 10, 30, 40, 5, 5]
        fear_amount = 150
        anger_amount = 200
        surprise_amount = 125

        result = experience_crowd(
            emotional_entity, fear_amount, anger_amount, surprise_amount
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [1, 1, 31, 41, 0, 22])

    # ########## PAD's emotional model test ##########

    # Test to verify successful update of fear, anger and surprise with positive amount for PAD model
    def test_successful_experience_crowd_positive_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        fear_amount = 2
        anger_amount = 10
        surprise_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 12, 15, 5, 22, 55, 90, 92])

    # Test to verify successful update of fear, anger and surprise with negative amount for PAD model
    def test_successful_experience_crowd_negative_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        fear_amount = -5
        anger_amount = -2
        surprise_amount = -2
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 5, 3, 5, 10, 55, 90, 92])

    # Test to verify update when all values and the emotional entity are null for PAD model
    def test_null_PAD(self):
        emotional_entity = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        fear_amount = 0
        anger_amount = 0
        surprise_amount = 0
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
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
        anger_amount = 5
        surprise_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
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
        anger_amount = 5
        surprise_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
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
        anger_amount = 5
        surprise_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
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
        anger_amount = 0
        surprise_amount = 0
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
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

    # Test to verify error due to non-integer fear, anger and surprise amount in PAD model
    def test_error_non_integer_fear_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        fear_amount = [30, "a"]
        anger_amount = 5
        surprise_amount = "10"
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
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
        anger_amount = 5
        surprise_amount = 10
        pleasure_amount = 5
        activation_amount = [30, "a"]
        dominance_amount = 82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    # Test to verify normalization of excessively negative fear, anger and surprise amount in PAD model
    def test_normalize_excessive_negative_fear_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        fear_amount = -60
        anger_amount = -70
        surprise_amount = -50
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 0, 0, 5, 0, 25, 90, 92])

    # Test to verify normalization of excessive emotional array for PAD model
    def test_normalize_excessive_array_PAD(self):
        emotional_entity = [10, 100, 10, 50, 87, 12, 50, 60, 10]
        fear_amount = 100
        anger_amount = 15
        surprise_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [2, 25, 27, 16, 22, 5, 55, 90, 92])

    # Test to verify normalization of excessive fear, anger and surprise amount for PAD model
    def test_normalize_excessive_fear_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        fear_amount = 300
        anger_amount = 500
        surprise_amount = 200
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [0, 0, 29, 48, 0, 20, 55, 90, 92])

    # Test to verify normalization of negative dominance amount in PAD model
    def test_normalize_negative_dominance_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        fear_amount = 2
        anger_amount = 4
        surprise_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = -82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 12, 9, 5, 22, 25, 90, 0])

    # Test to verify normalization of excessively high pleasure amount in PAD model
    def test_normalize_excessive_pleasure_amount_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        fear_amount = 2
        anger_amount = 4
        surprise_amount = 10
        pleasure_amount = 500
        activation_amount = 30
        dominance_amount = 82

        result = experience_crowd(
            emotional_entity,
            fear_amount,
            anger_amount,
            surprise_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [10, 10, 12, 9, 5, 22, 100, 90, 92])


if __name__ == "__main__":
    unittest.main()
