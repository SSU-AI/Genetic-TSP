'''
선택 : 엘리트 보존
input : 전체 유전자 리스트
output : 부모유전자

output의 첫 번째 인자가 elite 부모

적합도를 구하는 함수 필요 or 적합도 계산 함수 재정의 필요
'''
import numpy as np
import order_crossover_with_roulette_wheel as imp

def select_including_elite(candidates):
    fitness = []

    imp.open_cities()

    for candidate in candidates:
        fitness.append(60000 - imp.calculate_distance(candidate, imp.cities))

    # elite 구하기
    elite_ind = fitness.index(max(fitness))
    elite = candidates[elite_ind]

    # 새로운 fitness 리스트에서 elite의 fitness 제거
    new_fitness = fitness.copy()
    del new_fitness[elite_ind]

    # p2의 index 구하기
    p2_ind = fitness.index(max(new_fitness))    # 주의! new_fitness에는 elite의 fitness가 없기 때문에,
                                                # 2번째로 큰 fitness값을 new_fitness에서 찾고, 그 값의 인덱스는 fitness에서 찾아야 한다
    p2 = candidates[p2_ind]

    return [elite, p2]