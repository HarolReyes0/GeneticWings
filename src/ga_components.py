import random 
import numpy as np
import pandas as pd



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
                x(pd.Series): 
        """
        # Making predictions.
        y_hat = eval(self._genotype)

        # Calculating SSE
        error = x.astype("float64")[1:] - y_hat[:-1] 
        sse = sum(error)

        # return sse
        return sse
        
    def _mutate(self):
        pass

    def get_genotype(self):
        return self._genotype