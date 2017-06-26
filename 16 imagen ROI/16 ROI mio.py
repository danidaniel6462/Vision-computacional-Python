import cv2
import numpy as np
import matplotlib.pyplot as plt

bild = cv2.imread('pareja.jpg', cv2.IMREAD_COLOR)
roi = bild [15:300,330:550]      
bild [35:320,30:250] = roi
cv2.imshow('ORIGINAL',bild)

alphabild = cv2.imread('pareja.jpg', cv2.IMREAD_UNCHANGED)
graybild = cv2.imread('pareja.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('GRIS',graybild)

titles = ['Original', 'Alpha', 'Gray', 'Roi']
final = [bild, alphabild, graybild, roi]

for i in xrange(4):
    plt.subplot(2,2,i+1)
    plt.imshow(final[i])
    plt.title(title(titles[i]))
    plt.colorbar()
    plt.grid()
    plt.xticks([]), plt.yticks([])

plt.show()

#Cierre programa
cd = cv2.waitKey(0)
cv2.destroyAlWindows()
