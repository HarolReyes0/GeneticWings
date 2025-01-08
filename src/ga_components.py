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

        n_terms = random.randint(1, 100)

        # Randomly building the the ecuation that'll be use as genotype.
        for _ in range(n_terms):
            constant = random.randint(0, 10)
            operator = random.choice(['-', '+'])
            exponet = random.randint(-10, 10)
            term = f'{operator} {constant}x**{exponet} '

            self._genotype += term

    def _calculate_fitness(self, ecuation: str, x: pd.DataFrame) -> np.array:
        """
        """
        # Making predictions.
        y_hat = eval(ecuation)

        # Calculating SSE
        
    def _mutate(self):
        pass

    def get_genotype(self):
        return self._genotype