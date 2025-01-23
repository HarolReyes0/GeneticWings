import unittest
import numpy as np
from src.GAComponents import FitnessScoreMethods 

class TestFitnessScoreMethods(unittest.TestCase):
    def setUp(self):
        self.fitness_methods = FitnessScoreMethods()

    def test_make_predictions(self):
        # Define the input array and the equation as a string
        x = np.array([1, 2, 3, 4, 5])
        equation = "4*x**2 - 3*x**3"  # Example equation

        # Compute expected predictions using the equation
        y_hat = eval(equation)
        expected_output = x.astype("float64") - y_hat

        # Run the method
        result = self.fitness_methods._make_predictions(x, equation)

        # Assert the result matches the expected output
        np.testing.assert_array_almost_equal(result, expected_output)

if __name__ == "__main__":
    unittest.main()
