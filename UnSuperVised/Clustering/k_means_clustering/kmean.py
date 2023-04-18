# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:18:24 2023

@author: yusuf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



data = pd.read_csv('musteriler.csv')

X = data.iloc[:,3:].values

kmeans = KMeans ( n_clusters = 3, init = 'k-means++')
kmeans.fit(X)

print(kmeans.cluster_centers_)

result = []

for i in range(1,11):
    kmeans = KMeans (n_clusters = i, init='k-means++', random_state= 123)
    kmeans.fit(X)
    result.append(kmeans.inertia_)

plt.plot(range(1,11),result)
plt.xlabel("K value")
plt.ylabel("result")