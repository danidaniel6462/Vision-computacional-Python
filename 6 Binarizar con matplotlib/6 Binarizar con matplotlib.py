# BINARIZAR
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('osoFlash.jpg',0)
suavizar = cv2.medianBlur(img,5)
flag, umb1 = cv2.threshold(suavizar, 127, 255, cv2.THRESH_BINARY)
umb2 = cv2.adaptiveThreshold(suavizar,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
umb3 = cv2.adaptiveThreshold(suavizar,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titulos = ['Fuente Original ', 'Umbral General con 127',
           'Umbral adaptivo principal', 'Umbral adaptivo Gauss']
final = [suavizar, umb1, umb2, umb3]

for i in xrange(4):
    plt.subplot(2,2,i+1), plt.imshow(final[i],'gray')
    plt.title(titulos[i])
    plt.xticks([]),plt.yticks([])
plt.show()
