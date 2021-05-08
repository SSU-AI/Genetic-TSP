# 실행 섹션
from Envs import Env
from Calculations import Calculation as cal
from Crossovers import Crossover
from Selections import Selection
from Mutations import Mutation
from KCluster import KClustering as cluster
from Trees import Tree
import pandas as pd

output_chromosome = []

kcluster = cluster()

# 전체 city를 저장하는 객체, 초기화 및 결과 도출 시 사용된다.
df = pd.read_csv('TSP.csv', header=None, names=['x', 'y'])
init_env = Env(None, None)

# cluster의 갯수를 지정하는 변수
k=10
all_cluster, centroids, idxs_list = kcluster.kclustering(k, init_env, df)

# output은 list들을 저장하는 배열 / 각 list는 하나의 클러스터의 순열을 의미한다. (cluster 안의 도시에 대해서 최적의 경로를 저장한다.)
output = []

# 각 cluster에 대해서 유전 알고리즘을 적용시켜 학습한다.
for i in range(0, k):
    # i번째 cluster의 객체 및 초기화
    my_env = Env(all_cluster[i], idxs_list[i])
    my_env.init_candidates()

    # init_env에 정의된 만큼 학습을 진행한다
    for training_counter in range(init_env.num_of_training) :
        cal.calculate_fitness(my_env)
        cal.normalize_fitness(my_env)
        my_env.propagate_to_next_generation(Selection.roulette_wheel, Crossover.pmx,  Mutation.swap, my_env)

    # my_env의 population은 0~N/K 범위의 인덱스를 통해 표현한다. 따라서 이를 이용하여 오리지널 인덱스를 참조한다. 참조된 순열을 tmp_list에 저장하는 것
    tmp_list = []
    for i in (my_env.population[my_env.cur_max_idx]) :
        tmp_list.append(my_env.original_idx[i])
    # 오리지널 인덱스로 구성된 cluster "i"에 대한 순열이 완성되었고, 이를 output에 넣는다
    output.append(tmp_list)


# centroids를 통해 cluster간의 최적의 경로를 찾는다.
# tree_order는 tree_search를 통해 얻은 centroids간의 최적의 경로
tree_list = [0] * (k)
tree_min, tree_order =  Tree.tree_search(tree_list, centroids, 0, k)

# tree search를 통해 얻은 cluster간의 최적의 경로와 최적화 된 cluster를 이용하여 최종 결과물을 도출해낸다.
final_order = []
for i in tree_order :
    final_order += output[i]

# final_order는 최종결과물 (tree_search를 통해 얻은 cluster 순서와 최적화된 cluster의 유전자를 결합하여 생성됨)
print(final_order)
print('final cost : ' + str(cal.calculate_total_distance(final_order, init_env.cities))) 







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

for i in reversed(range(0, 10)):
    my_env.sol += output_chromosome[i]


city = []
with open('TSP.csv', mode='r', newline='') as tsp:
    reader = csv.reader(tsp)
    for row in reader:
        city.append(row)

total_cost = cal.calculate_total_distance(my_env.sol, city)

print('final cost: ' + str(total_cost))
