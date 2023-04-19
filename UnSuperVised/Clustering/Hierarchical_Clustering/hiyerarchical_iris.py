# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:23:06 2023

@author: yusuf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering  ## cluster
import scipy.cluster.hierarchy as sch
from sklearn.cluster import KMeans


data = pd.read_csv("iris.csv")
print(data.head())
print(data.columns)

## drop Id columns
data = data.drop(["Id", "Species"], axis = 1)
print(data.head())


## model
cluster = AgglomerativeClustering(n_clusters = 3, metric = "euclidean", linkage = "ward")    
##cluster = AgglomerativeClustering(n_clusters = 3, affinity = "euclidean", linkage = "ward")    
predict = cluster.fit_predict(data)

## dendogram
dendogram = sch.dendrogram(sch.linkage(data, method = "ward"))
plt.show()

## plot
data = data.values
plt.scatter(data[predict==0,0],data[predict==0,1],s=100,color='red')
plt.scatter(data[predict==1,0],data[predict==1,1],s=100,color='blue')
plt.scatter(data[predict==2,0],data[predict==2,1],s=100,color='green')
plt.title('Hierarchical Clustering Iris Dataset')
plt.show()


######### for KMeans


kmeans = KMeans(n_clusters = 3, init = 'k-means++')
kmeans.fit(data)

print(kmeans.cluster_centers_)
sonuclar = []
for i in range(1,11):
    kmeans = KMeans (n_clusters = i, init='k-means++', random_state= 123)
    kmeans.fit(data)
    sonuclar.append(kmeans.inertia_)

plt.plot(range(1,11),sonuclar)
plt.show()

kmeans = KMeans (n_clusters = 3, init='k-means++', random_state= 123)
Y_tahmin= kmeans.fit_predict(data)
print(Y_tahmin)  
plt.scatter(data[Y_tahmin==0,0],data[Y_tahmin==0,1],s=100, c='red')
plt.scatter(data[Y_tahmin==1,0],data[Y_tahmin==1,1],s=100, c='blue')
plt.scatter(data[Y_tahmin==2,0],data[Y_tahmin==2,1],s=100, c='green')
plt.scatter(data[Y_tahmin==3,0],data[Y_tahmin==3,1],s=100, c='yellow')
plt.title('KMeans')
plt.show()
