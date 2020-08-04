# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 21:13:19 2017

@author: samarth
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,1,5,8,1,9,2,6] ,dtype = np.float64)
y = np.array([2,1,8,8,8,0,6,11] ,dtype = np.float64)

plt.scatter(x,y)
plt.show