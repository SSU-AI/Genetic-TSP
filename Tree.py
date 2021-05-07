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
        for i in range(num_of_cluster) :
            if i not in visited_list :
                visited_list[now_depth] = i
                tmp_min = min(tmp_min, tree_search(visited_list, centroid, now_depth+1))
                visited_list[now_depth] = 0
        return tmp_min
