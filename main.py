from ga_components import *
import pandas as pd

x = pd.Series([3, 4, 5, 6])

individual = Individual()

individual._create_genotype()

score = individual._calculate_fitness(x)

print("Fitness score", score)