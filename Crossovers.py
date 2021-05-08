import numpy as np
import random

class Crossover:
    @staticmethod
    def cycle(parent1, parent2):
        # 처음에 자식의 값들을 모두 -1로 초기화
        child = [-1 for i in range(len(parent1))]
        ind = 0
        first, second = parent1, parent2
        while True:
            # 자식의 값이 모두 채워지면 종료
            if child.count(-1)==0:
                break
            # first가 가리키는 부모의 유전자들이 child에 기록됨
            child[ind] = first[ind]
            ind = first.index(second[ind])
            # 싸이클 완성시
            if child[ind]!=-1 and child.count(-1)!=0:
                # first <-> second 교환
                first, second = second, first
                # ind는 자식 염색체에서 채워지지 않은(-1) 제일 앞 인덱스
                ind = child.index(-1)

        return child

    @staticmethod
    def pmx(parent1, parent2):
        point1 = random.randint(int(len(parent1)/10), int(len(parent1 * 9)/10) - 2)
        point2 = random.randint(point1 + 1, int(len(parent1 * 9)/10))
        np1 = np.array(parent1, np.int32)
        np2 = np.array(parent2, np.int32)
        child = np.concatenate((parent2[:point1], parent1[point1:point2], parent2[point2:]), axis=0)
        child = child.astype(np.int32)
        
        no_duplicate = False
        while no_duplicate == False:
            no_duplicate = True
            target = child[point1:]
            for i in range(0, point1):
                if child[i] in target:
                    no_duplicate = False
                    idx = np.where(np1 == child[i])[0]
                    child[i] = np2[idx]
                    
            target = child[:point2]
            for i in range(point2, len(parent1)):
                if (child[i] in target):
                    no_duplicate = False
                    idx = np.where(np1 == child[i])[0]
                    child[i] = np2[idx]
        
        return child.tolist()


    @staticmethod
    def crossover_order(parent1, parent2) : 
        start_idx = random.randint(0, len(parent1) - 1)
        end_idx = random.randint(start_idx+1, len(parent1))
        new_list = parent1[start_idx:end_idx].copy()
        tmp_set = set()
        for i in range(len(new_list)) :
            tmp_set.add(new_list[i])
        for i in range(len(parent2)) :
            if parent2[i] not in tmp_set :
                tmp_set.add(parent2[i])
                new_list.append(parent2[i])
        return new_list
