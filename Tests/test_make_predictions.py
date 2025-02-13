import pytest
import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.GAComponents import FitnessScoreMethods

@pytest.mark.parametrize(
    "x, equation, expected_output",
    [
        (
            [1, 2, 3, 4, 5],
            "4*x**2 - 3*x**3",
            [1, -8, -45, -128, -275]
        ),
        (
            [0, 1, 2, 3, 4],
            "2*x**3 - 0.5*x**2 + 3*x - 4",
            [-4, 0.5, 16, 54.5, 128]
        ),
        (
            [1, 2, 3, 4, 5],
            "np.log(x+2) * x**2 + np.sin(x)",
            [
                1.94008327,  
                6.45447487,  
                14.62606122, 
                27.91134901, 
                47.68882945  
            ]
        )
    ]
)
def test_make_predictions(x, equation, expected_output):
    # Initialize the FitnessScoreMethods object
    fitness_methods = FitnessScoreMethods()

    # Convert input to numpy array
    x = np.array(x)

    # Run the method
    result = fitness_methods._make_predictions(x, equation)

    # Assert the result matches the expected output
    np.testing.assert_array_almost_equal(result, expected_output)