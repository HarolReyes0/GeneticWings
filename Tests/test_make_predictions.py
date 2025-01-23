import pytest
import numpy as np
from src.GAComponents import FitnessScoreMethods

# TODO: Fix importation bug. 

@pytest.mark.parametrize(
    "x, equation",
    [
        ([1, 2, 3, 4, 5], "4*x**2 - 3*x**3")
    ]
)
def test_make_predictions(x, equation):
    # Initialize the FitnessScoreMethods object
    fitness_methods = FitnessScoreMethods()

    # Convert input to numpy array
    x = np.array(x)

    # Compute expected predictions using the equation
    y_hat = eval(equation)
    expected_output = x.astype("float64") - y_hat

    # Run the method
    result = fitness_methods._make_predictions(x, equation)

    # Assert the result matches the expected output
    np.testing.assert_array_almost_equal(result, expected_output)

