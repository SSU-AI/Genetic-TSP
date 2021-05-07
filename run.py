# 실행 섹션
from Envs import Env
from Calculations import Calculation as cal
from Crossovers import Crossover
from Selections import Selection
from Mutations import Mutation

my_env = Env()
my_env.open_cities()
my_env.init_random_candidates()
cal.calculate_fitness(my_env)
cal.normalize_fitness(my_env)
my_env.propagate_to_next_generation(Selection.roulette_wheel, Crossover.pmx,  Mutation.inversion, my_env)
print('final cost : ' + str(cal.calculate_total_distance(my_env.population[my_env.cur_min_idx], my_env.cities))) 


# if(is_training == 0):
#     open_soution(sol[0])
#     print('final cost : ' + str(calculate_total_distance(sol, cities))) 
# else :
#     visited_list = [-1] * num_of_cluster
#     print(tree_search(visited_list, cities, 0))
# =============================================================================
#     init_random_candidates(population)
#     for i in range(num_of_training) :
#         print(calculate_total_distance(population[cur_min_idx], cities))
#         population = propagate_to_next_generation(population, fitness, cities).copy()
#     print(total_min_fit)
# =============================================================================
    
"""
Tree 호출 부분

all_cluster, centroids = KClustering(10)

#centroids shape= [centroidsID][x좌표, y좌표]

# i 번째 cluster 에 속해 있는 cities들
# 1D vector [chromosome]
chromosome = all_cluster[i]
"""
