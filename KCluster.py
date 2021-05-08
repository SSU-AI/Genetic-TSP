import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

class KClustering:

    @staticmethod
    def kclustering(k, env):
        df = pd.read_csv('TSP.csv', header=None, names=['x', 'y'])

        models = KMeans(n_clusters = k)
        models.fit(df)

        labels = models.predict(df)
        centroids = models.cluster_centers_

        df["cluster"] = np.array(labels)

        # plt.scatter(df.x, df.y, c=labels, alpha=0.5)
        # plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='b')
        # plt.show()

        cities_of_cluster = []
        idxs_list = []
        centroids_of_cluster = centroids
        for i in range(0, k):
            tmp = [cities for cities in df[df['cluster'] == i].index]
            idxs_list.append(tmp)
            tmp_list = []
            for k in range(0, len(tmp)) :
                tmp_list.append(env.cities[k])
            cities_of_cluster.append(tmp_list)


        return cities_of_cluster, centroids_of_cluster, idxs_list
