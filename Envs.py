import csv
import random

class Env :
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

    def open_cities(self) :
        with open('TSP.csv', mode='r', newline='') as tsp:
            reader = csv.reader(tsp)
            for row in reader :
                self.cities.append(row)

    def open_soution(self) :
        with open('example_solution.csv', mode='r', newline='') as solution :
            reader = csv.reader(solution)
            for row in reader :
                self.sol.append(int(row[0]))
            idx = self.sol.index(0)
            front = self.sol[idx:]
            back = self.sol[0:idx]
            self.sol= front + back
            self.sol.append(int(0))

    def init_random_candidates(self, population) : 
        order = []
        for i in range (self.num_of_cities) :
            order.insert(i, i)
        for i in range (self.num_of_population) :
            tmp_order = []
            tmp_order = order.copy()
            random.shuffle(tmp_order)
            population.insert(i, tmp_order)

    def propagate_to_next_generation(self, selection_method, cross_over_method, mutation_method) :
        new_population = []
        for idx in range (num_of_population):

            list_A = pick_random_population(self.population, self.fitness).copy()
            list_B = pick_random_population(self.population, self.fitness).copy()

            new_list = cross_over_method(list_A, list_B).copy()
            mutation_method(new_list, mutation_rate)
            new_population.append(new_list)
        self.population = new_population.copy()
    