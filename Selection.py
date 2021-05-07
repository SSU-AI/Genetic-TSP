import numpy as np
import random

class Selection:     
    @staticmethod
    def tournament(t=0.7, k=8, env):
        tournament = np.random.randint(0, env.num_of_population, 2**k)

        for i in reversed(range(1, r+1)):
            for j in range(0, 2**(i-1)):
                random_value = random.random()
                # 적합도 좋은 거 선택
                if t > random_value:
                    if env.fitness[tournament[2*j]] > env.fitness[tournament[2*j+1]]:
                        tournament[j] = tournament[2*j]
                    else:
                        tournament[j] = tournament[2*j+1]
                #적합도 안 좋은 거 선택
                else:
                    if env.fitness[tournament[2*j]] < env.fitness[tournament[2*j+1]]:
                        tournament[j] = tournament[2*j]
                    else:
                        tournament[j] = tournament[2*j+1]

        parent = tournament[0]
        return parent

    @staticmethod
    def ranking(N=14, env):
        highest_chrom_idx = env.get_highest_chroms(N, env)
        
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

    @staticmethod
    def get_highest_chroms(n, env):
        fit_list_sorted = sorted(env.fitness)
        highest_ch_idx = []
        
        for i in range(n):
            highest_fitness = fit_list_sorted.pop()
            highest_ch_idx.append(env.fitness.index(highest_fitness))
        
        return highest_ch_idx

    @staticmethod
    def elite_include(env):
        fitness = env.fitness.copy()

        # elite 구하기
        elite_ind = fitness.index(max(fitness))
        elite = env.population[elite_ind]

        # 새로운 fitness 리스트에서 elite의 fitness 제거
        new_fitness = fitness.copy()
        del new_fitness[elite_ind]

        # p2의 index 구하기
        p2_ind = fitness.index(max(new_fitness))    # 주의! new_fitness에는 elite의 fitness가 없기 때문에,
                                                    # 2번째로 큰 fitness값을 new_fitness에서 찾고, 그 값의 인덱스는 fitness에서 찾아야 한다
        p2 = env.population[p2_ind]

        return [elite, p2]

    @staticmethod
    def roulette_wheel(env):
        now_idx = 0
        random_value = random.random()
        while (random_value > 0) :
            random_value -= env.fitness[now_idx]
            now_idx = now_idx + 1
        now_idx = now_idx - 1
        return env.population[now_idx]