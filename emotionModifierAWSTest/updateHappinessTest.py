import unittest
from AWSLambdaConnection import update_happiness


class TestUpdateHappiness(unittest.TestCase):
    ########## Paul Ekman individual testing part ##########
    def test_successful_updateHappiness_positive_amount(self):
        # Input values
        emotional_entity = [10, 0, 0, 0, 0, 0]
        happiness_amount = 30

        # Call updateHappiness function
        result = update_happiness(emotional_entity, happiness_amount)

        # Check that the result is not None
        self.assertIsNotNone(result)
        # Check that the result is of the expected type
        self.assertIsInstance(result, list)
        # Check if the result has the expected size
        self.assertEqual(len(result), 6)
        # Expected response
        self.assertEqual(result, [40, 0, 0, 0, 0, 0])

    def test_successful_updateHappiness_negative_amount(self):
        emotional_entity = [50, 0, 0, 0, 0, 0]
        happiness_amount = -10

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [40, 0, 0, 0, 0, 0])

    def test_error_excessive_happiness_amount(self):
        emotional_entity = [10, 10, 30, 40, 5, 5]
        happiness_amount = 100

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "The total sum of emotions cannot exceed 100")

    def test_error_excessive_array(self):
        emotional_entity = [200, 10, 30, 40, 5, 5]
        happiness_amount = 10

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "The total sum of emotions cannot exceed 100")

    def test_error_excessive_array_2(self):
        emotional_entity = [10, 10, 30, 400, 5, 5]
        happiness_amount = 10

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "The total sum of emotions cannot exceed 100")

    def test_error_non_integer_array(self):
        emotional_entity = ["a", 10, 30, 40, 5, 5]
        happiness_amount = 10

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    def test_error_non_integer_array_2(self):
        emotional_entity = [[0, 2], 10, 30, 40, 5, 5]
        happiness_amount = 10

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    def test_error_non_integer_happiness_amount(self):
        emotional_entity = [50, 10, 0, 0, 0, 0]
        happiness_amount = "a"

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    def test_error_negative_array(self):
        emotional_entity = [-10, 10, 30, 5, 0, 6]
        happiness_amount = 10

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    def test_error_negative_array_2(self):
        emotional_entity = [10, 10, 30, -5, 0, 6]
        happiness_amount = 10

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    def test_error_excessive_negative_amount(self):
        emotional_entity = [10, 10, 30, 5, 0, 6]
        happiness_amount = -15

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Emotions cannot be negative")

    def test_null(self):
        emotional_entity = [0, 0, 0, 0, 0, 0]
        happiness_amount = 0

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [0, 0, 0, 0, 0, 0])

    def test_error_array_positions(self):
        emotional_entity = [0, 0, 0, 0]
        happiness_amount = 0

        result = update_happiness(emotional_entity, happiness_amount)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotEqual(len(result), 6)
        self.assertEqual(
            result,
            "The list of emotions must have 6 positions for the Paul Ekman model or 9 positions for the PAD model",
        )

    ########## Test part in conjunction with Paul Ekman and PAD ##########
    def test_successful_updateHappiness_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        happiness_amount = 30
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [40, 10, 10, 5, 5, 12, 55, 90, 92])

    def test_excessive_amount_error_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        happiness_amount = 300
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "The total sum of emotions cannot exceed 100")

    def test_excessive_amount_error_PAD_2(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 50, 60, 10]
        happiness_amount = 30
        pleasure_amount = 500
        activation_amount = 30
        dominance_amount = 82

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "PAD values cannot be less than 0 or greater than 100")

    def test_excessive_array_error_PAD(self):
        emotional_entity = [10, 100, 10, 50, 87, 12, 50, 60, 10]
        happiness_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "The total sum of emotions cannot exceed 100")

    def test_non_integer_array_error_PAD(self):
        emotional_entity = [10, 10, "10", 5, 5, 12, 50, 60, 10]
        happiness_amount = 30
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    def test_non_integer_array_error_PAD_2(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, "G", 60, 10]
        happiness_amount = 30
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    def test_non_integer_amount_error_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        happiness_amount = [30, "a"]
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    def test_non_integer_amount_error_PAD_2(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        happiness_amount = 8
        pleasure_amount = 5
        activation_amount = [30, "a"]
        dominance_amount = 82

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "All amounts must be integers")

    def test_negative_array_error_PAD(self):
        emotional_entity = [-10, 10, 10, 5, 5, 12, 20, -60, 10]
        happiness_amount = 10
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(
            result, "The list of emotions must contain only positive integers or zero"
        )

    def test_negative_amount_error_PAD(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        happiness_amount = -60
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = 82

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Emotions cannot be negative")

    def test_negative_amount_error_PAD_2(self):
        emotional_entity = [10, 10, 10, 5, 5, 12, 20, 60, 10]
        happiness_amount = 2
        pleasure_amount = 5
        activation_amount = 30
        dominance_amount = -82

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "PAD values cannot be less than 0 or greater than 100")

    def test_null_PAD(self):
        emotional_entity = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        happiness_amount = 0
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = update_happiness(
            emotional_entity,
            happiness_amount,
            pleasure_amount,
            activation_amount,
            dominance_amount,
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 9)
        self.assertEqual(result, [0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_array_positions_error_PAD(self):
        emotional_entity = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        happiness_amount = 0
        pleasure_amount = 0
        activation_amount = 0
        dominance_amount = 0

        result = update_happiness(
            emotional_entity,
            happiness_amount,
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


if __name__ == "__main__":
    unittest.main()
