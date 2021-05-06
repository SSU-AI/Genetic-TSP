'''
교배 : PMX
input : (부모 유전자1, 부모 유전자2)
output : 자식유전자
'''

import numpy as np

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