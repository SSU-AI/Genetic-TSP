# 실행 섹션
from Inits import Init as env
from Calculations import Calculation as cal

my_env = env()
my_cal = cal()
my_env.open_cities()
my_env.open_soution()
print('final cost : ' + str(my_cal.calculate_total_distance(env.sol, env.cities))) 
my_env.init_random_candidates(my_env.population)
my_cal.calculate_fitness(my_env)
my_cal.nomalize_fitness(my_env)

# for i in range(num_of_training) :
#     print(calculate_total_distance(population[cur_min_idx], cities))
#     population = propagate_to_next_generation(population, fitness, cities).copy()
# print(total_min_fit)

# if(is_training == 0):
#     open_soution(sol[0])
#     print('final cost : ' + str(calculate_total_distance(sol, cities))) 
# else :
#     visited_list = [-1] * num_of_cluster
#     print(tree_search(visited_list, cities, 0))
# =============================================================================
#     init_random_candidates(population)
#     for i in range(num_of_training) :
#         calculate_fitness(fitness, population, cities, total_min_fit, cur_min_fit)
#         nomalize_fitness(fitness)
#         print(calculate_total_distance(population[cur_min_idx], cities))
#         population = propagate_to_next_generation(population, fitness, cities).copy()
#     print(total_min_fit)
# =============================================================================
    
