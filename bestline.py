# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:47:51 2017

@author: samarth
"""
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

a = np.array([2,4,6,7,8,2], dtype = np.float64)
b = np.array([1,4,7,2,5,8], dtype = np.float64)

def bestline(a,b):
    t = (mean(a) * mean(b) - mean(a*b)) /(mean(a) * mean(a) - mean(a*a))
    p= mean(b) - mean(a) * t
    return t,p
    
t,p = bestline(a,b)


plt.scatter(a,b)
plt.plot(a,bestline)
plt.show
print(t,p)    