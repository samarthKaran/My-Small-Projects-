# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 21:33:37 2017

@author: samarth
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 

x = np.array([[1,2],[1.5,1.8],[5,8],[8,8],[1,0.6],[9,11],[2,3],[1.5,4],[6,3],[2,7],[4,4],[5,3]] , dtype = np.float64)

clf = KMeans(n_clusters = 4)
clf.fit(x)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = ["g.", "r.","y.","b."]
for i in range(len(x)):
     plt.plot(x[i][0],x[i][1],colors[labels[i]])
     
plt.scatter(centroids[:,0],centroids[:,1],marker='x',s=250)
plt.show ()