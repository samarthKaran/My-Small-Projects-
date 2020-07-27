# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 09:44:04 2017

@author: samarth
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2

cap = cv2.VideoCapture(0)#accessing camera
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
