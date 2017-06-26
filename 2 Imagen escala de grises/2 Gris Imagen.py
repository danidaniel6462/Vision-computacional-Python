import cv2

img = cv2.imread('pareja.jpg')
gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Hola PY', img)
cv2.imshow('DGris',gris)
cv2.imwrite('dgris.jpg',gris)

cv2.waitKey(0);					
cv2.destroyAllWindows()		
