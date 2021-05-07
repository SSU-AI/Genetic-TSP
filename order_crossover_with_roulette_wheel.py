import numpy as np
import csv
import random

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


