import numpy as np
class Calculation :
    @staticmethod
    def calculate_distance(point_1,point_2):
        dist = np.linalg.norm(np.array(point_1) - np.array(point_2))
        return dist

    @staticmethod
    def calculate_total_distance(sol, cities) : 
        total_cost = 0
        for idx in range(len(sol)-1) :
            pos_city_1 = [float(cities[sol[idx]][0]), float(cities[sol[idx]][1])]
            pos_city_2 = [float(cities[sol[idx+1]][0]), float(cities[sol[idx+1]][1])]         
            dist = Calculation.calculate_distance(pos_city_1, pos_city_2)
            total_cost += dist
        return total_cost

    @staticmethod
    def calculate_fitness(my_env) :
        cur_min_fit = my_env.INF
        for idx in range (my_env.num_of_population):
            fit_val = 1 / (Calculation.calculate_total_distance(my_env.population[idx], my_env.cities) + 1)
            my_env.fitness.insert(idx, fit_val)
            if(my_env.fitness[idx] > my_env.cur_min_fit) :
                my_env.cur_min_fit = my_env.fitness[idx]
        if(cur_min_fit < my_env.total_min_fit) :
            my_env.total_min_fit = cur_min_fit
            my_env.cur_min_idx = idx

    @staticmethod
    def normalize_fitness(my_env) :
        fit_sum = 0
        for idx in range (my_env.num_of_population) :
            fit_sum  += my_env.fitness[idx]
        for idx in range (my_env.num_of_population) :
            my_env.fitness[idx] = my_env.fitness[idx] / fit_sum 
     
