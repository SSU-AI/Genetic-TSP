'''
교배 : 싸이클(Cycle)
input : 부모 유전자1, 부모 유전자2
output : 자식유전자

parent1, parent2의 순서에 따라 결과가 달라짐에 주의

'''
import numpy as np

def crossover_with_cycle(parent1, parent2):
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