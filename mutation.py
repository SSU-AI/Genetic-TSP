'''
돌연변이 : inversion, swap
input : 자식유전자
output : (새로운) 자식유전자

함수마다 변이가 일어날 확률 추가 필요

'''
import numpy as np

def inversion(offspring):
    ind1, ind2 = sorted(np.random.choice([i for i in range(len(offspring))], 2, replace=False))
    end = [] if ind2==len(offspring)-1 else offspring[ind2+1:]
    return offspring[:ind1] + list(reversed(offspring[ind1:ind2+1])) + end



def swap(offspring):
    ind1, ind2 = np.random.choice([i for i in range(len(offspring))], 2, replace=False)
    offspring[ind1], offspring[ind2] = offspring[ind2], offspring[ind1]
    return offspring

print(inversion([0,1,2,3,4,5,6,7,8,9]))