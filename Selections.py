import numpy as np
import random

class Selection:     
    @staticmethod
    def tournament(env):
        t=env.tournament_t
        n= env.tournament_n
        tournament = np.random.randint(0, env.num_of_population, 2**n)

        for i in reversed(range(1, n+1)):
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
        return env.population[parent]

    @staticmethod
    def ranking(env):
        N=5
        highest_chrom_idx = Selection.get_highest_chroms(N, env)
        prob_list = [0.3, 0.25, 0.2, 0.15, 0.1]
        p = random.random()
        sum = 0
        for i in range(N):
            sum += prob_list[i]
            if sum >= p:
                idx = i
                break
        return env.population[highest_chrom_idx[idx]]

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

        # print(env.elite_fitness, len(env.elite))
        # 이전 세대로부터 전달받을 값이 있을 때
        if env.elite_fitness!=0:
            ## 하나 더 추가하지 말고, 랜덤으로 한개의 population에 넣기
            random_ind = np.random.randint(len(env.population))
            env.population[random_ind]=env.elite
            env.fitness[random_ind] = env.elite_fitness

        ## elite, elite_fitness 구하기
        # 최대 적합도의 값
        env.elite_fitness = max(env.fitness)
        # 최대 적합도를 갖는 유전자의 index
        elite_ind = env.fitness.index(env.elite_fitness)
        # 최대 적합도를 갖는 유전자 리스트
        env.elite = env.population[elite_ind]

        # population 중에서 random으로 1개 리턴
        return env.population[np.random.randint(len(env.population))]

    @staticmethod
    def roulette_wheel(env):
        now_idx = 0
        random_value = random.random()
        while (random_value > 0) :
            random_value -= env.fitness[now_idx]
            now_idx = now_idx + 1
        now_idx = now_idx - 1
        return env.population[now_idx]