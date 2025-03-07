import random 
import numpy as np
import pandas as pd
import re

# TODO:
# Create a class to store all mutation methods ().
# Create a class to store all crossover methods.

class FitnessScoreMethods:
    # Calculates the error between the predicted values and the target values.
    calculate_error = lambda x, y_hat: x.astype("float64") - y_hat

    def _make_predictions(self, x: np.array, f: str) -> np.array:
        """
            Generate predictions based on a given function.

            This method evaluates the provided function string `f` using Python's `eval`
            and calculates the difference between the input array `x` (converted to 
            float64) and the evaluated predictions.

            Parameters:
                x (np.array): Input array of numerical features.
                f (str): A string representing the function to generate predictions.

            Returns:
                np.array: The differences between `x` (starting from the second element)
                        and the predicted values (excluding the last element).
        """
        y_hat = eval(f)

        return y_hat
    
    def _sse(self, x: np.array, f: str) -> float:
        """
            Calculate the Sum of Squared Errors (SSE) for predictions.

            This method computes the Sum of Squared Errors based on the difference
            between actual values and predicted values generated using `_make_predictions`.

            Parameters:
                x (np.array): Input array of numerical features.
                f (str): A string representing the function to generate predictions.

            Returns:
            float: The calculated Sum of Squared Errors.
        """
        y_hat = self._make_predictions(x, f)

        error = calculate_error(x.astype("float64")[1:], y_hat[:-1])

        return sum(np.square(error))
    
    def _mse(self, x: np.array, f: str) -> float:
        """
            Calculates the Mean Squared Error (MSE) of the predictions.

            This method computes the Mean Squared Error based on the difference
            between actual values and predicted values generated using `_make_predictions`.

            Parameters:
                x (np.array): Input array of numerical features.
                f (str): A string representing the function to generate predictions.

            Returns:
            float: The calculated Mean Squared Error.
        """
        y_hat = self._make_predictions(x, f)

        error = calculate_error(x.astype("float64"), y_hat)
        
        return np.mean(np.square(error[1:-1]))
    
    def _mae(self, x: np.array, f: str) -> float:
        """
            Calculates the Mean Absolute Error (MAE) of the predictions.

            This method computes the Mean Absolute Error based on the difference
            between actual values and predicted values generated using `_make_predictions`.

            Parameters:
                x (np.array): Input array of numerical features.
                f (str): A string representing the function to generate predictions.

            Returns:
            float: The calculated Mean Absolute Error.
        """
        y_hat = self._make_predictions(x, f)

        error = calculate_error(x.astype("float64"), y_hat)
        
        return np.mean(np.abs(error[1:-1]))
    
    @staticmethod
    def _fitness_not_found(*args):
        """
            Raises an error.
        """
        raise ValueError("Evaluation metric not found.")


class Individual(FitnessScoreMethods):
    def __init__(self, genotype = ''):
        self._genotype = genotype
        self.__fitness_score = []

    def _create_genotype(self):
        """
            Randomly creates the equation that will be use as the genotype.

            Inputs:
                None
            Returns:
                None  
        """

        n_terms = random.randint(1, 10)

        # Randomly creating the the equation that'll be use as genotype.
        for _ in range(n_terms):
            constant = random.randint(1, 9)
            operator = random.choice(['-', '+'])
            exponent = random.randint(-9, 9)
            term = f'{operator} {constant} * x**{np.float64(exponent)} '

            self._genotype += term

    def _calculate_fitness(self, x: pd.Series, method = 'sse') -> float:
        """
            Based on the user preferences an evaluation method that will be used as fitness score.
            The available options are: 
                Mean Absolute Error(MAE)
                Mean Squared Error (MSE)
                Sum of Squared Error (SSE)

            Inputs:
                x(pd.Series): features to use for the predictions.
                method(str): metric that will be use to evaluate the fitness score.
            Outputs:
                float: indicating the sum of squared error.
        """
        methods = {
                    'sse' : self._sse,
                    'mse' : self._mse,
                    'mae' : self._mae,
                    }
        
        # Selecting the method to calculate the fitness score.
        method = methods.get(method.lower(), self._fitness_not_found)

        return method(x, self._genotype)
        
    def _mutate(self, p_mutation = 5):
        """
        """

        # Finding all constants and exponents in the equation.
        constants = re.findall("[-+] [0-9]", self._genotype)
        exponents = re.findall("x\*\*\s*([+-]?\d+(?:\.\d+)?)", self._genotype)

        if random.randint(0, 100) <= p_mutation:
            pass 

        

    def get_genotype(self):
        return self._genotype