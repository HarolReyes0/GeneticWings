from random import randint




class Individual:
    def __init__(self, genotype = None):
        self._genotype = genotype
        self.__fitness_score = []

    def _create_genotype(self):
        pass

    def _calculate_fitness(self):
        pass

    def _mutate(self):
        pass

    def get_genotype(self):
        pass