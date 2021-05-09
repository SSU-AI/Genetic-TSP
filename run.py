# 실행 섹션
from Envs import Env
from Calculations import Calculation as cal
from Crossovers import Crossover
from Selections import Selection
from Mutations import Mutation
from KCluster import KClustering as cluster
from Trees import Tree
import pandas as pd

kcluster = cluster()

# 전체 city를 저장하는 객체, 초기화 및 결과 도출 시 사용된다.
df = pd.read_csv('TSP.csv', header=None, names=['x', 'y'])
init_env = Env(None, None)

# cluster의 갯수를 지정하는 변수, k개의 cluster를 만든다. 
# all_cluster[i] -> i번째 클러스터의 모든 cities
# centroids[i] -> i번째 클러스터의 centroid (중심점)
# idxs_list[i] -> i번째 클러스터의 실제 인덱스 (all_cluster는 0~1000/k, idxs_list는 0~1000)

k=10
all_cluster, centroids, idxs_list = kcluster.kclustering(k, init_env, df)
gen_count=10


final_order = []
cluster_order = []
child_cluster_order = []
child_cluster = []
child_centroids = []
child_idxs_list = []

# centroids에 대한 tree search로 최적의 cluster path를 찾는다
tree_list = [0] * k
tree_min, total_tree_order = Tree.tree_search(tree_list, centroids, 0, len(tree_list))


# 하나의 cluster를 child_k개의 cluster로 또 나눈다.
child_k = 7             #PARAMETER
output = []
for i in range(0, k):
    # 각 cluster에 대한 환경을  만들어 준다.
    kluster_env = Env(all_cluster[i], idxs_list[i])

    # 하나의 big cluster를 child_k개의 small cluster로 나누어 준다.
    input_df = pd.DataFrame(all_cluster[i])
    child_cluster_points, child_centroids, tmp_child_idxs = kcluster.kclustering(child_k, kluster_env, input_df)

    # big cluster의 결과를 저장할 리스트
    cluster_order = []
    for now_child in range (child_k) :
        # small cluster에 대해 환경을 만들어 준다.
        child_env = Env(child_cluster_points[now_child], tmp_child_idxs[now_child])
        child_env.init_candidates()

        # small cluster를 학습시킨다
        count = gen_count-1
        fits = []
        for training_counter in range(100):
            cal.calculate_fitness(child_env)
            fits.append(child_env.total_max_fit)
            if len(fits)>1:
                if fits[-1]==fits[-2]:
                    count -= 1
                else:
                    count=gen_count-1
            if count==0:
                fits = []
                break
            cal.normalize_fitness(child_env)
            child_env.propagate_to_next_generation(Selection.elite_include, Crossover.pmx, Mutation.inversion, child_env)
            
        # 학습 시킨 small cluster의 결과를 cluster_order에 저장한다
        tmp_lists = []
        for el in child_env.population[child_env.cur_max_idx] :
            tmp_lists.append(child_env.original_idx[el])
        cluster_order.append(tmp_lists)
        
    # i번째 big cluster에 속한 small cluster 간의 최적의 경로를 찾는다
    tree_list = [0] * len(child_centroids)
    tree_min, tree_order = Tree.tree_search(tree_list, child_centroids, 0, len(tree_list))
    
    # tree search로 얻은 tree_order를 통해 small cluster를 병합한다.
    # 이렇게 나온 cluster_output은 original_idx를 활용할 것이다.
    cluster_output = []
    for now_tree_num in tree_order :
        for last_cluster_el in cluster_order[now_tree_num] :
            cluster_output.append(idxs_list[i][last_cluster_el])

    # 최종적으로 output에 big cluster의 결과를 저장한다
    output.append(cluster_output)

# big cluster의 최적 경로 output과 tree search를 통해 얻은 total_tree_order를 통해 1차원의 최적의 경로, final_order를 얻는다
final_order = []
for now_tree in total_tree_order :
    final_order += output[now_tree]

# 결과를 출력한다
print(len(final_order))    
print(final_order)
print('final cost : ' + str(cal.calculate_total_distance(final_order, init_env.cities)))    