import numpy as np
import csv
import random
import numpy as np

# 선언 섹션
is_training = 1
INF = 10000000000
total_min_fit = INF 
cur_min_fit = INF
cur_min_idx = -1
num_of_cities = 1000 # according to data, num(cities) is 1000
num_of_population = 500
num_of_training = 100
num_of_cluster = 10
mutation_rate = 0.01
cities = []
sol = []
fitness = []
population = []


# 정의 섹션
# 1. init

def open_cities(cities) :
    with open('TSP.csv', mode='r', newline='') as tsp:
        reader = csv.reader(tsp)
        for row in reader :
            cities.append(row)

def open_soution(sol) :
    with open('example_solution.csv', mode='r', newline='') as solution :
        reader = csv.reader(solution)
        for row in reader :
            sol.append(int(row[0]))
        idx = sol.index(0)
        front = sol[idx:]
        back = sol[0:idx]
        sol= front + back
        sol.append(int(0))

def init_random_candidates(population) : 
    order = []
    for i in range (num_of_cities) :
        order.insert(i, i)
    for i in range (num_of_population) :
        tmp_order = []
        tmp_order = order.copy()
        random.shuffle(tmp_order)
        population.insert(i, tmp_order)

# 2. calculation

def calculate_distance(point_1,point_2):
    dist = np.linalg.norm(np.array(point_1) - np.array(point_2))
    return dist

def calculate_total_distance(sol, cities) : 
    total_cost = 0;    
    for idx in range(len(sol)-1) :
        pos_city_1 = [float(cities[sol[idx]][0]), float(cities[sol[idx]][1])]
        pos_city_2 = [float(cities[sol[idx+1]][0]), float(cities[sol[idx+1]][1])]         
        dist = calculate_distance(pos_city_1, pos_city_2)
        total_cost += dist
    return total_cost

def calculate_fitness(fitness, population, cities, total_min_fit, cur_min_fit) :
    cur_min_fit = INF
    for idx in range (num_of_population):
        fit_val = 1 / (calculate_total_distance(population[idx], cities) + 1)
        fitness.insert(idx, fit_val)
        if(fitness[idx] < cur_min_fit) :
            cur_min_fit = fitness[idx]
    if(cur_min_fit < total_min_fit) :
        total_min_fit = cur_min_fit
        cur_min_idx = idx
    print(total_min_fit)

def nomalize_fitness(fitness) :
    fit_sum = 0
    for idx in range (num_of_population) :
       fit_sum  += fitness[idx]
    for idx in range (num_of_population) :
       fitness[idx] = fitness[idx] / fit_sum 
     
# 3. propagation

def pick_random_population(population, fitness) :
    now_idx = 0
    random_value = random.random()
    while (random_value > 0) :
        random_value -= fitness[now_idx]
        now_idx = now_idx + 1
    now_idx = now_idx - 1
    return population[now_idx]
    

def cross_over(list_A, list_B) : 
    start_idx = random.randint(0, num_of_cities-1)
    end_idx = random.randint(start_idx+1, num_of_cities)
    new_list = list_A[start_idx:end_idx].copy()
    tmp_set = set()
    for i in range(len(new_list)) :
        tmp_set.add(new_list[i])
    for i in range(len(list_B)) :
        if list_B[i] not in tmp_set :
            tmp_set.add(list_B[i])
            new_list.append(list_B[i])
    return new_list

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


def propagate_to_next_generation(population, fitness, cities) :
    new_population = []
    for idx in range (num_of_population):
        list_A = pick_random_population(population, fitness).copy()
        list_B = pick_random_population(population, fitness).copy()
        new_list = cross_over(list_A, list_B).copy()
        mutate(new_list, mutation_rate)
        new_population.append(new_list)
    return  new_population.copy()
    

def tree_search(visited_list, centroid,now_depth):
    if(now_depth == num_of_cluster) :
        return calculate_total_distance(visited_list, centroid)
    tmp_min = INF
    for i in range(num_of_cluster) :
        if i not in visited_list :
            visited_list[now_depth] = i
            tmp_min = min(tmp_min, tree_search(visited_list, centroid, now_depth+1))
            visited_list[now_depth] = 0
    return tmp_min


# 실행 섹션
open_cities(cities)
if(is_training == 0):
    open_soution(sol[0])
    print('final cost : ' + str(calculate_total_distance(sol, cities))) 
else :
    visited_list = [-1] * num_of_cluster
    print(tree_search(visited_list, cities, 0))
# =============================================================================
#     init_random_candidates(population)
#     for i in range(num_of_training) :
#         calculate_fitness(fitness, population, cities, total_min_fit, cur_min_fit)
#         nomalize_fitness(fitness)
#         print(calculate_total_distance(population[cur_min_idx], cities))
#         population = propagate_to_next_generation(population, fitness, cities).copy()
#     print(total_min_fit)
# =============================================================================
    
