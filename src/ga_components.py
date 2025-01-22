import random 
import numpy as np
import pandas as pd
import re

# TODO:
# Create a class to store all fitness methods (SSE, MSE, MAE).
# Create a class to store all mutation methods ().
# Create a class to store all crossover methods.

class FitnessScoreMethods:
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

        return x.astype("float64")[1:] - y_hat[:-1]
    
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
        error = self._make_predictions(x, f)
        
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
        error = self._make_predictions(x, f)
        
        return np.mean(np.square(error))
    
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
        error = self._make_predictions(x, f)
        
        return np.mean(np.abs(error))


class Individual:
    def __init__(self, genotype = ''):
        self._genotype = genotype
        self.__fitness_score = []

    def _create_genotype(self):
        """
            Randomly creates the ecuation that will be use as the genotype.

            Inputs:
                None
            Returns:
                None  
        """

        n_terms = random.randint(1, 10)

        # Randomly creating the the ecuation that'll be use as genotype.
        for _ in range(n_terms):
            constant = random.randint(1, 9)
            operator = random.choice(['-', '+'])
            exponet = random.randint(-9, 9)
            term = f'{operator} {constant} * x**{np.float64(exponet)} '

            self._genotype += term

    def _calculate_fitness(self, x: pd.Series) -> float:
        """
            Calculates the sum of squared error of the individual.

            Inputs:
                x(pd.Series): features to use for the predictions.
            Outputs:
                float: indicating the sum of squared error.
        """
        # Making predictions.
        y_hat = eval(self._genotype)

        # Calculating SSE
        error = x.astype("float64")[1:] - y_hat[:-1] 
        sse = sum(error)

        # return sse
        return sse
        
    def _mutate(self, p_mutation = 5):
        """
        """

        # Finding all constants and exponets in the ecuation.
        constants = re.findall("[-+] [0-9]", self._genotype)
        explonets = re.findall("x\*\*\s*([+-]?\d+(?:\.\d+)?)", self._genotype)

        if random.randint(0, 100) <= p_mutation:
            pass 

        

    def get_genotype(self):
        return self._genotype