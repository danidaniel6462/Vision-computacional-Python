                            # DETECCION SOBEL OPENCV
import cv2
import numpy as np

Comedian = cv2.imread('comedian.jpg',cv2.IMREAD_COLOR)
grisComedian = cv2.cvtColor(Comedian, cv2.COLOR_BGR2GRAY)
Comedian = cv2.GaussianBlur(grisComedian,(15,15),0)
Lap = cv2.Laplacian(Comedian,cv2.CV_64F)
MGx = cv2.Sobel(Comedian,cv2.CV_64F,1,0,ksize = 5)
MGy = cv2.Sobel(Comedian,cv2.CV_64F,0,1,ksize = 5)
DetBordes = Lap + MGx + MGy
cv2.imshow('SUMA BORDES',DetBordes)
cv2.imwrite('bordes.jpg',DetBordes)
ComedianBinarizada = cv2.imread('bordes.jpg',cv2.IMREAD_GRAYSCALE)
_,bina = cv2.threshold (ComedianBinarizada,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('BINARIZADO',bina)
cv2.waitKey(0)
cv2.destroyAllWindows()
