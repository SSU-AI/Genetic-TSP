import numpy as np
import random

class Selection:
    def __init__(self, fitness, population, num_of_population):
        self.fitness = fitness
        self.population = population
        self.num_of_population = num_of_population
        

    def tournament(self, t=0.7, k=8):
        tournament = np.random.randint(0, self.num_of_population, 2**k)

        for i in reversed(range(1, r+1)):
            for j in range(0, 2**(i-1)):
                random_value = random.random()
                # 적합도 좋은 거 선택
                if t > random_value:
                    if self.fitness[tournament[2*j]] > self.fitness[tournament[2*j+1]]:
                        tournament[j] = tournament[2*j]
                    else:
                        tournament[j] = tournament[2*j+1]
                #적합도 안 좋은 거 선택
                else:
                    if self.fitness[tournament[2*j]] < self.fitness[tournament[2*j+1]]:
                        tournament[j] = tournament[2*j]
                    else:
                        tournament[j] = tournament[2*j+1]

        parent = tournament[0]
        return parent

    def ranking(self, N=14):
        highest_chrom_idx = self.get_highest_chroms(N)
        
        p = random.random()
        sum = 0
        for i in range(N):
            sub = N-i
            if i < 5:
                sub -= 1

            sum += sub/100

            if sum >= p:
                idx = i
                break
                
        return highest_chrom_idx[idx]

    def get_highest_chroms(self, n):
        fit_list_sorted = sorted(self.fitness)
        highest_ch_idx = []
        
        for i in range(n):
            highest_fitness = fit_list_sorted.pop()
            highest_ch_idx.append(self.fitness.index(highest_fitness))
        
        return highest_ch_idx


    def elite_include(self):
        fitness = []

        imp.open_cities()
        ## 적합도 함수 물어보기*-----------------------------------------------
        ## 만약 사전에 구한 적합도들 사용 시
        #      1. 모든 fitness => self.fitness
        #      2. fitness구하는 코드 지우기(아래)
        for candidate in self.population:
            fitness.append(60000 - imp.calculate_distance(candidate, imp.cities))
        #----------------------------------------------------------------------
        # elite 구하기
        elite_ind = fitness.index(max(fitness))
        elite = self.population[elite_ind]

        # 새로운 fitness 리스트에서 elite의 fitness 제거
        new_fitness = fitness.copy()
        del new_fitness[elite_ind]

        # p2의 index 구하기
        p2_ind = fitness.index(max(new_fitness))    # 주의! new_fitness에는 elite의 fitness가 없기 때문에,
                                                    # 2번째로 큰 fitness값을 new_fitness에서 찾고, 그 값의 인덱스는 fitness에서 찾아야 한다
        p2 = self.population[p2_ind]

        return [elite, p2]

    def roulette_wheel(self):
        now_idx = 0
        random_value = random.random()
        while (random_value > 0) :
            random_value -= self.fitness[now_idx]
            now_idx = now_idx + 1
        now_idx = now_idx - 1
        return self.population[now_idx]