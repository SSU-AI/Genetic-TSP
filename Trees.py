import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
from Calculations import Calculation

class Tree :
    @staticmethod
    def tree_search(visited_list, centroid,now_depth, num_of_cluster):
        if(now_depth == num_of_cluster - 1) :
            return Calculation.calculate_total_distance(visited_list, centroid), visited_list
        tmp_min = 100000000
        new_list = []
        for i in range(num_of_cluster) :
            if i not in visited_list :
                search_result = 0
                visited_list[now_depth] = i
                search_result, tmp_list = Tree.tree_search(visited_list, centroid, now_depth+1, num_of_cluster)
                if(tmp_min > search_result) :
                    tmp_min = search_result
                    new_list = tmp_list.copy()

                visited_list[now_depth] = 0
        return tmp_min, new_list
