# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 00:35:40 2017

@author: samarth
"""

import nummy as np
import pandas as pd
import math 
import matplotlib , plyplot as plt
from collectors import counter

dataset = { 'i' = [[1,3],[2,5],[3,1]] , 'j' = [[2,4],[5,6],[7,1]]} 
new_data = [6,5]

def k_nrst_ngbh(data,predict,k=3):
    if len(data) > k :
        warning.warn('k does not have specific value')
        distance = []
        for group in data:
            for features in data[group]:
                e_dis = no.sqrt(np.sum(np.array(features) - no.array(predict)))
                distance.append([e_dis,group])
                
                dis = [i[1]] for i in sorted(distance)[:k]]
            print(counter(dis).most_common(1))
            dis_result = counter(dis).most_common(1)[0][0]
            return dis_result
 
result =   k_nrst_ngbh(dataset , new_data , k=3)
print(result)