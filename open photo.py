# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:06:58 2017

@author: samarth
"""

import numpy as np
import cv2

img = cv2.imread('Screenshot (1).png', cv2.IMREAD_COLOR)
cv2.line(img,(5,5),(100,100),(255,255,255),15)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
