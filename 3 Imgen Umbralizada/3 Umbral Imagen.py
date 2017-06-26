import cv2
import numpy as np

img = cv2.imread('pareja.jpg')
gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Hola PY', img)
cv2.imshow('DGris',gris)
cv2.imwrite('dgris.jpg',gris)
min = np.array([5,50,50],np.uint8)
max = np.array([15,255,255],np.uint8)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
umbral = cv2.inRange(hsv,min,max)
cv2.imshow('Color',umbral)
cv2.imwrite('color.jpg',umbral)

cv2.waitKey(0)
cv2.destroyAllWindows()
