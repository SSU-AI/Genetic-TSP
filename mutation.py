class Mutation :
    def swap(target_list, idx_A, idx_B) :
        tmp_val = target_list[idx_A]
        target_list[idx_A] = target_list[idx_B]
        target_list[idx_B] = tmp_val 

    def mutate(target_list, mutation_rate) :
        for i in range(0, num_of_cities) :
            if(random.random() < mutation_rate):
                mutation_idx = random.randint(0, num_of_cities-1)
                next_idx = (mutation_idx  + 1) % num_of_cities
                swap(target_list, mutation_idx, next_idx)
