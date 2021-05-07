# 실행 섹션
from Envs import env as env
from Calculations import Calculation as cal

my_env = env()
my_env.open_cities()

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
    
"""
Tree 호출 부분

all_cluster, centroids = KClustering(10)

#centroids shape= [centroidsID][x좌표, y좌표]

# i 번째 cluster 에 속해 있는 cities들
# 1D vector [chromosome]
chromosome = all_cluster[i]
"""
