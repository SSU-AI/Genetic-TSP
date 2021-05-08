import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

class Tree :
    @staticmethod
    def tree_search(visited_list, centroid,now_depth):
        if(now_depth == num_of_cluster) :
            return calculate_total_distance(visited_list, centroid)
        tmp_min = INF
        new_list = []
        for i in range(num_of_cluster) :
            if i not in visited_list :
                visited_list[now_depth] = i
                next_search, tmp_list = tree_search(visited_list, centroid, now_depth+1)
                if(tmp_min > next_search)
                {
                    tmp_min = next_search
                    new_list = tmp_list.copy()
                }
                visited_list[now_depth] = 0
        return tmp_min, new_list
