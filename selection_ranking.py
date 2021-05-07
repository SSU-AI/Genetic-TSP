'''
선택 : 랭킹
input : 전체 유전자 리스트
output : 부모유전자

선택할 상위 유전자 개수 N=14로 설정
사전 확률(순위순( : 13 12 11 10 9 9 8 7 6 5 4 3 2 1)) 상위 14개

적합도를 구하는 함수 필요(get_fitness())
'''
import random

def get_parent_by_ranking(chrom_list):
    N = 14
    chrom_list = chrom_list.copy()
    fitness_list = get_fitness_list(chrom_list)
    highest_chrom_idx, highest_fitness_sum = get_highest_chroms(N, fitness_list)
    
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
    
def get_fitness_list(ch_list):
    fit_list = []
    for chrom in ch_list:
        fit_list.append(get_fitness(chrom))
    return fit_list
    
def get_highest_chroms(n, fit_list):
    fit_list_sorted = sorted(fit_list)
    highest_ch_idx = []
    highest_fitness_sum = 0
    
    for i in range(n):
        highest_fitness = fit_list_sorted.pop()
        highest_fitness_sum += highest_fitness
        highest_ch_idx.append(fit_list.index(highest_fitness))
    
    return highest_ch_idx, highest_fitness_sum