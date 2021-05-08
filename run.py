# 실행 섹션
from Envs import Env
from Calculations import Calculation as cal
from Crossovers import Crossover
from Selections import Selection
from Mutations import Mutation
from KCluster import KClustering as cluster


k=10
output_chromosome = []

kcluster = cluster()
init_env = Env(None)
all_cluster, centroids = kcluster.kclustering(k, init_env)

for i in range(0, k):
    # i번째 cluster
    my_env = Env(all_cluster[i])
    my_env.init_candidates()
    cal.calculate_fitness(my_env)
    cal.normalize_fitness(my_env)
    my_env.propagate_to_next_generation(Selection.roulette_wheel, Crossover.pmx,  Mutation.swap, my_env)

    cal.calculate_fitness(my_env)   # 마지막 연산 후, population 갱신
    output_chromosome.append(my_env.population[my_env.cur_max_idx])

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

ex) tree 순서 0, 1, 2, 3, 4, 5, 6, 7, 8 ,9 이면
    my_env.sol = output_choromosome[0] + output_choromosome[1] + ...

# i 번째 cluster 에 속해 있는 cities들
# 1D vector [chromosome]
chromosome = all_cluster[i]
"""
print(output_chromosome[0])
print(output_chromosome[1])
