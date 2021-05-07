import numpy as np
import csv
import random

# 3. propagation

def pick_random_population(population, fitness) :
    now_idx = 0
    random_value = random.random()
    while (random_value > 0) :
        random_value -= fitness[now_idx]
        now_idx = now_idx + 1
    now_idx = now_idx - 1
    return population[now_idx]
    