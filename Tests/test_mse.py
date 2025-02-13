import pytest 
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.GAComponents import FitnessScoreMethods

def test_mse(x, y_hat, expected_result):
    fitness_methods = FitnessScoreMethods()
