import random 




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
            constant = random.randint(0, 100)
            operator = random.choice(['-', '+'])
            term = f'{operator} {constant}x '

            self._genotype += term


    def _calculate_fitness(self):
        pass

    def _mutate(self):
        pass

    def get_genotype(self):
        return self._genotype