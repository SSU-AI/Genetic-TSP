'''
선택 : 토너먼트
input : 전체 유전자 리스트 population
output : 부모유전자 1개

x1 > x2 적합도 가정 할 때, 
    if(t > random) then select x1;
    else select x2

2^k개의 유전자 선택한 다음, 토너먼트 경쟁으로 최종적으로 하나의 해 선택

Hyperparameter
    t : 0~1 사이 실수. t 값이 높을수록 선택압이 높아짐. t가 0.5 근처이거나 이보다 작은 것은 비합리적.
    k : 0이상 정수. K 값이 클수록, 토너먼트 참가하는 유전자가 많을수록 선택압이 높아짐.

'''

import numpy as np
import random

fitness = []
population = []
num_of_population = 500

def tournament_selection(fitness, t=0.7, k=8):

tournament = np.random.randint(0, num_of_population, 2**k)

for i in reversed(range(1, r+1)):
    for j in range(0, 2**(i-1)):
        random_value = random.random()
        # 적합도 좋은 거 선택
        if t > random_value:
            if fitness[tournament[2*j]] > fitness[tournament[2*j+1]]:
                tournament[j] = tournament[2*j]
            else:
                tournament[j] = tournament[2*j+1]
        #적합도 안 좋은 거 선택
        else:
            if fitness[tournament[2*j]] < fitness[tournament[2*j+1]]:
                tournament[j] = tournament[2*j]
            else:
                tournament[j] = tournament[2*j+1]

parent = tournament[0]
return parent