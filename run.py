# 실행 섹션
from Envs import Env
from Calculations import Calculation as cal
from Crossovers import Crossover
from Selections import Selection
from Mutations import Mutation
from KCluster import KClustering as cluster
from Trees import Tree
import pandas as pd

#output_chromosome = []

kcluster = cluster()

# 전체 city를 저장하는 객체, 초기화 및 결과 도출 시 사용된다.
df = pd.read_csv('TSP.csv', header=None, names=['x', 'y'])
init_env = Env(None, None)

# cluster의 갯수를 지정하는 변수
k=10
all_cluster, centroids, idxs_list = kcluster.kclustering(k, init_env, df)

"""
# output은 list들을 저장하는 배열 / 각 list는 하나의 클러스터의 순열을 의미한다. (cluster 안의 도시에 대해서 최적의 경로를 저장한다.)
output = []
"""

final_order = []
cluster_order = []
child_cluster_order = []
child_cluster = []
child_centroids = []
child_idxs_list = []

# cluster를 한 번 더 나눈다.
for i in range(0, k):
    child_k=10
    input_df = pd.DataFrame(all_cluster[i])
    child_cluster, child_centroids, child_idxs_list = kcluster.kclustering(child_k, init_env, input_df)

    # cluster_cluster 안의 list들을 저장하는 배열 / 각 list는 cluster_cluster 안의 하나의 클러스터의 순열을 의미한다. (cluster of cluster 안의 도시에 대해서 최적의 경로를 저장한다.)
    child_cluster_cluster_output = []
    for j in range(0, child_k):
        my_env = Env(child_cluster[j], child_idxs_list[j])
        my_env.init_candidates()

        for training_counter in range(init_env.num_of_training):
            cal.calculate_fitness(my_env)
            cal.normalize_fitness(my_env)
            my_env.propagate_to_next_generation(Selection.roulette_wheel, Crossover.crossover_order, Mutation.swap, my_env)

        tmp_list = []
        for i in (my_env.population[my_env.cur_max_idx]):
            tmp_list.append(my_env.original_idx[i])
        child_cluster_cluster_output.append(tmp_list) # (j, 클러스터의 클러스터의 순열)

    tree_list = [0] * len(child_centroids)
    tree_min, tree_order = Tree.tree_search(tree_list, child_centroids, 0, len(tree_list))

    child_cluster_cluster_order = []
    for j in tree_order:
        child_cluster_cluster_order.append(child_cluster_cluster_output[j]) # (ordered j, 클러스터의 클러스터의 순열)
    
    child_cluster_order.append(child_cluster_cluster_order) # (k, ordered j, 클러스터의 클러스터의 순열)

tree_list = [0] * k
tree_min, tree_order = Tree.tree_search(tree_list, centroids, 0, len(tree_list))

for i in tree_order:
    cluster_order.append(child_cluster_order[i]) # (ordered k, ordered j, 클러스터의 클러스터의 순열)

print(len(cluster_order))
print(len(cluster_order[0]))
print(len(cluster_order[0][0]))

final_order = [i for j in cluster_order for k in j for i in k]

print(final_order)

print(final_order)
print('final cost : ' + str(cal.calculate_total_distance(final_order, init_env.cities))) 


"""

# 각 cluster에 대해서 유전 알고리즘을 적용시켜 학습한다.
for i in range(0, k):
    # i번째 cluster의 객체 및 초기화
    my_env = Env(all_cluster[i], idxs_list[i])
    my_env.init_candidates()

    # init_env에 정의된 만큼 학습을 진행한다
    for training_counter in range(init_env.num_of_training) :
        cal.calculate_fitness(my_env)
        cal.normalize_fitness(my_env)
        my_env.propagate_to_next_generation(Selection.roulette_wheel, Crossover.crossover_order,  Mutation.swap, my_env)

    # my_env의 population은 0~N/K 범위의 인덱스를 통해 표현한다. 따라서 이를 이용하여 오리지널 인덱스를 참조한다. 참조된 순열을 tmp_list에 저장하는 것
    tmp_list = []
    for i in (my_env.population[my_env.cur_max_idx]) :
        tmp_list.append(my_env.original_idx[i])
    # 오리지널 인덱스로 구성된 cluster "i"에 대한 순열이 완성되었고, 이를 output에 넣는다
    output.append(tmp_list)

# output[i] -> centroids [i] 중심으로 가지는 군집 내 도시 index

input_df = pd.DataFrame(centroids)

a, b, c = \
    kcluster.kclustering(10, init_env, input_df)


# idx_list_of_cluster[i] : i번째 군집에 속하는 centroids 들 리스트


# centroids를 통해 cluster간의 최적의 경로를 찾는다.
# tree_order는 tree_search를 통해 얻은 centroids간의 최적의 경로
total_tree_order = []
for i in range(10): # 10개의 cluster에 대한 각각의 orders
    
    tree_list = [0] * (len(c[i]))
    tree_min, tree_order =  Tree.tree_search(tree_list, a[i], 0, len(tree_list))

    order = []
    for j in tree_order:
        order.append(c[i][j])
    
    total_tree_order.append(order)
# 0~9 클러스터당 ordered 된 100개의 기존 클러스터들

tree_list = [0] * (10)
tree_min, tree_order = Tree.tree_search(tree_list, b, 0, 10)

order = []
for i in tree_order:
    order.append(total_tree_order[i])

final_order = []

for i in order:
    for j in i:
        final_order += output[j]

# tree search를 통해 얻은 cluster간의 최적의 경로와 최적화 된 cluster를 이용하여 최종 결과물을 도출해낸다.
# final_order = []
# for i in tree_order :
#     final_order += output[i]

# final_order는 최종결과물 (tree_search를 통해 얻은 cluster 순서와 최적화된 cluster의 유전자를 결합하여 생성됨)
print(final_order)
print('final cost : ' + str(cal.calculate_total_distance(final_order, init_env.cities))) 


"""




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

"""
print(output_chromosome[0])
print(output_chromosome[1])

for i in reversed(range(0, 10)):
    my_env.sol += output_chromosome[i]


city = []
with open('TSP.csv', mode='r', newline='') as tsp:
    reader = csv.reader(tsp)
    for row in reader:
        city.append(row)

total_cost = cal.calculate_total_distance(my_env.sol, city)

print('final cost: ' + str(total_cost))
"""