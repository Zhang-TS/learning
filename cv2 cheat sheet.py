# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 22:53:50 2017

@author: tazhang


This cheat sheet contains common functions used in cv2

version2
"""

import cv2

# read image in 
img = cv2.imread('Lenna.png') # in original color
img_gray = cv2.imread('Lenna.png',0) # in grayscale


# plot image
cv2.imshow('Lenna', img_gray)

# wait for a few ms
cv2.waitKey(0)  # waiting time in ms, 0 for infinity

# close an image window
cv2.destroyWindow('Lenna')

# write to image
cv2.imwrite('Lenna_grayscale.jpg', img_gray)



