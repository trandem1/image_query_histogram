import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.orig/10.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[64],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()