import numpy as np

class Mutation :
    @staticmethod
    def swap(target_list, idx_A, idx_B) :
        tmp_val = target_list[idx_A]
        target_list[idx_A] = target_list[idx_B]
        target_list[idx_B] = tmp_val 

    @staticmethod
    def mutate(target_list, mutation_rate) :
        for i in range(0, num_of_cities) :
            if(random.random() < mutation_rate):
                mutation_idx = random.randint(0, num_of_cities-1)
                next_idx = (mutation_idx  + 1) % num_of_cities
                swap(target_list, mutation_idx, next_idx)

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
