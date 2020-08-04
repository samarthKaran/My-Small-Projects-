# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:06:52 2017

@author: samarth
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('opencv-feature-matching-image.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('opencv-feature-matching-template.jpg',cv2.IMREAD_COLOR)#comparing one img with grp of pictures

orb = cv2.ORB_create()#fn called Orb to create img

kp1, des1 = orb.detectAndCompute(img1,None)#fn called from orb for img1 nd img2 to detect and compute
kp2, des2 = orb.detectAndCompute(img2,None)#des1 and des 2 are grp of imges

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)#fn called norm_hamming, croosscheck to access a particular feature..all stored in bf

matches = bf.match(des1,des2)#grp of imges are compared
matches = sorted(matches, key = lambda x:x.distance)#sorting and lamba is predefine fn that will give distance of cluster of 1 img in 1 grp and another img in another grp

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)#flag = 2 for 2 images and img3 is created and drawmatches takes img 1 and its keypt and img2 and its keyplot and it plots ten different points
plt.imshow(img3)#show
plt.show()



#cv2.line(img,(0,0),(150,150),(255,255,255),15)

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()