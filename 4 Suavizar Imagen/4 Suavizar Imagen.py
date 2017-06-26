# SUAVIZAR
import cv2
import numpy as np

img = cv2.imread('osoFlash.jpg')
cv2.imshow('Osito',img)
suavizado = cv2.medianBlur(img,15)    # los valores de la function MedianBlur
cv2.imshow('Suavizado', suavizado)   # tienen que ser impares  

cv2.waitKey(0)
cv2.destroyAllWindows()
