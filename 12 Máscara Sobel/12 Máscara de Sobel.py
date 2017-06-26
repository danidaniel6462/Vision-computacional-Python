                            # MASCARA DE SOBEL
import cv2
import numpy as np

imaComedian = cv2.imread('comedian.jpg',cv2.IMREAD_UNCHANGED)
cv2.imshow('Comedian Original',imaComedian)
[x , y, z] = imaComedian.shape

MGx = np.zeros((x , y, z), dtype = float)
MGy = np.zeros((x , y, z), dtype = float)

SumaSobel = np.zeros((x , y, z), dtype = float)

v = np.array([[ 1, 2, 1],
              [ 0, 0, 0],
              [-1,-2,-1]], dtype = float)
h = np.array([[1, 0, -1],
              [2, 0, -2],
              [1, 0, -1]], dtype = float)

i = 1
j = 1
k = 0
aux = 0

for k in range(z-1):
    for i in range(x-1):
        for j in range(y-1):
            aux = h[0,0]*imaComedian[i-1,j-1,k]+h[0,1]*imaComedian[i,j-1,k]+h[0,2]*imaComedian[i+1,j-1,k]+h[1,0]*imaComedian[i-1,j,k]+h[1,1]*imaComedian[i,j,k]+h[1,2]*imaComedian[i+1,j,k]+h[2,0]*imaComedian[i-1,j+1,k]+h[2,1]*imaComedian[i,j+1,k]+h[2,2]*imaComedian[i+1,j+1,k]
            MGx[ i, j, k] = abs(aux)
            aux = v[0,0]*imaComedian[i-1,j-1,k]+v[0,1]*imaComedian[i,j-1,k]+v[0,2]*imaComedian[i+1,j-1,k]+v[1,0]*imaComedian[i-1,j,k]+v[1,1]*imaComedian[i,j,k]+v[1,2]*imaComedian[i+1,j,k]+v[2,0]*imaComedian[i-1,j+1,k]+v[2,1]*imaComedian[i,j+1,k]+v[2,2]*imaComedian[i+1,j+1,k]
            MGy[ i, j, k] =  abs(aux)

SumaSobel = MGx + MGy

cv2.imwrite('SUMA SOBEL.jpg',SumaSobel)

GrisComedian = cv2.imread('SUMA SOBEL.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Gris Comedian',GrisComedian)
_,bina = cv2.threshold (GrisComedian,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Comedian Binarizado',bina)

ComedianSobel = cv2.imread('SUMA SOBEL.jpg',cv2.IMREAD_COLOR)
cv2.imshow('Comedian Sobel',ComedianSobel)
cv2.waitKey(0) 
cv2.destroyAllWindows()

