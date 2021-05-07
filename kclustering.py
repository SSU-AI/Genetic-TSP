import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd


def KClustering(k=10):
    df = pd.read_csv('TSP.csv', header=None, names=['x', 'y'])

    kmeans = KMeans(n_clusters = k)
    kmeans.fit(df)

    labels = kmeans.predict(df)
    centroids = kmeans.cluster_centers_

    df["cluster"] = np.array(labels)

    plt.scatter(df.x, df.y, c=labels, alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='b')
    plt.show()

    cities_of_cluster = []
    centroids_of_cluster = centroids
    for i in range(0, k):
        tmp = [cities for cities in df[df['cluster'] == i].index]
        cities_of_cluster.append(tmp)

    return cities_of_cluster, centroids_of_cluster

all_cluster, centroids = KClustering(10)

#centroids shape= [centroidsID][x좌표, y좌표]

# i 번째 cluster 에 속해 있는 cities들
# 1D vector [chromosome]
chromosome = all_cluster[i]

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


