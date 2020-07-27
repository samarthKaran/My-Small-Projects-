# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 09:40:56 2017

@author: samarth
"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0)#fn in cv2 accessing camera no. 0
while(True):
    ret, frame = cap.read()#calling read which is accessed by camera using cap and ret is returning to the system
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#calling fn Color convering it to gray
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])#lower and upper are range of colorsfrom 0 to 255
   
   
    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)
   
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
   # cv2.imshow('frame',gray)#gray is value above
    if cv2.waitKey(1) & 0xFF == ord('q'):#pressing q will destry the window
        break
    
cap.release()
cv2.destroyAllWindows()
        
