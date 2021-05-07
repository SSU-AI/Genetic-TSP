import csv
import random

class Init :
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
