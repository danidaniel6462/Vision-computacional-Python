        # BINARIZAR MEDIA Y VARIANZA
import cv2
import numpy as np
from matplotlib import pyplot as plt

oso = cv2.imread('osoFlash.jpg',cv2.IMREAD_UNCHANGED)
alphaoso = cv2.imread('osoFlash.jpg',cv2.IMREAD_GRAYSCALE)
grisoso = cv2.imread('osoFlash.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Oso',oso)
cv2.imshow('Gris',alphaoso)

[x , y] = grisoso.shape
O = grisoso

OSO_A = np.matrix(O)
OSO_B = OSO_A.getA1()

suma = 0
for m in range(OSO_B.shape[0]):
    sumatorio = suma + OSO_B[m]
    
media = np.sum(OSO_B,dtype = np.float32)/OSO_B.size;      # Media

for n in range(OSO_B.shape[0]):
    suma = suma + (float(OSO_B[n])-media)** 2

varianza = np.sqrt(float(suma)/OSO_B.size)               # Varianza

for i in range(x):
    for j in range(y):
        if (O[i,j] > varianza):
            O[i,j] = 255
        else:
            O[i,j] = 0

cv2.imshow('Oso Final Binarizado :3',grisoso)

print 'RGB      :', oso.shape
print 'ARGB     :', alphaoso.shape
print 'gris     :', grisoso.shape
print 'img.dtype:', oso.dtype
print 'img.size :', oso.dtype
print 'MEDIA    : ',media
print 'VARIANZA : ',varianza

cv2.waitKey(0)
cv2.destroyAllWindows()
