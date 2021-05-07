import numpy as np

class Mutation :
    @staticmethod
    def inversion(offspring):
        ind1, ind2 = sorted(np.random.choice([i for i in range(len(offspring))], 2, replace=False))
        end = [] if ind2==len(offspring)-1 else offspring[ind2+1:]
        return offspring[:ind1] + list(reversed(offspring[ind1:ind2+1])) + end

    @staticmethod
    def swap(offspring):
        ind1, ind2 = np.random.choice([i for i in range(len(offspring))], 2, replace=False)
        offspring[ind1], offspring[ind2] = offspring[ind2], offspring[ind1]
        return offspring
