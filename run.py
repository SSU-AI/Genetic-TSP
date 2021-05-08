# 실행 섹션
from Envs import Env
from Calculations import Calculation as cal
from Crossovers import Crossover
from Selections import Selection
from Mutations import Mutation
from KCluster import KClustering as cluster
from Trees import Tree

k=10
output_chromosome = []

kcluster = cluster()
init_env = Env(None, None)
all_cluster, centroids, idxs_list = kcluster.kclustering(k, init_env)
output = []
for i in range(0, k):
    # i번째 cluster
    my_env = Env(all_cluster[i], idxs_list[i])
    my_env.init_candidates()
    cal.calculate_fitness(my_env)
    cal.normalize_fitness(my_env)
    my_env.propagate_to_next_generation(Selection.roulette_wheel, Crossover.crossover_order,  Mutation.swap, my_env)

    cal.calculate_fitness(my_env)   # 마지막 연산 후, population 갱신

    tmp_list = []
    for i in (my_env.population[my_env.cur_min_idx]) :
        tmp_list.append(my_env.original_idx[i])
    output.append(tmp_list)
print(output)

tree_list = [0] * (k)
tree_min, tree_order =  Tree.tree_search(tree_list, centroids, 0, k)

final_order = []
for i in tree_list :
    final_order += output[i]
print('final cost : ' + str(cal.calculate_total_distance(final_order, init_env.cities))) 

# print(tree_min, tree_order)


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
# print(output_chromosome[0])
# print(output_chromosome[1])
