import numpy as np

class Mating:
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
        def get_child_by_pmx(chrom1, chrom2):
    point1 = int(len(chrom1) / 3)
    point2 = point1 * 2
    np1 = np.array(chrom1)
    np2 = np.array(chrom2)
    
    child = np.concatenate((chrom2[:point1], chrom1[point1:point2], chrom2[point2:]), axis=0)
    
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
        for i in range(point2, len(chrom1)):
            if (child[i] in target):
                no_duplicate = False
                idx = np.where(np1 == child[i])[0]
                child[i] = np2[idx]
    
    return child.tolist()


    @staticmethod
    def corssover_order(list_A, list_B) : 
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