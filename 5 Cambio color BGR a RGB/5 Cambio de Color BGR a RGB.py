# CAMBIO BGR a RGB
import cv2
import numpy as np

img = cv2.imread('osoFlash.jpg')
cv2.imshow('BGR',img)

b,g,r = cv2.split(img)
BGRaRGB = cv2.merge([r,g,b])
cv2.imshow('RGB', BGRaRGB) 

cv2.waitKey(0)
cv2.destroyAllWindows()
