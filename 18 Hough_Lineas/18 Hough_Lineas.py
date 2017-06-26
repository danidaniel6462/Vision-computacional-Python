import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

imgOriginal = cv2.imread('dave.png')
cv2.imshow('Imagen Original', imgOriginal)
img = cv2.imread('dave.png')
grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(grises, 50, 150, apertureSize = 3)

lineas = cv2.HoughLines(bordes, 1, np.pi/180, 200)

for rho, theta in lineas[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*(a))
    x2 = int(x0-1000*(-b))
    y2 = int(y0-1000*(a))

    cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 2)

titles = ['ORIGINA', 'TRANSFORMADA DE HOUGH_LINEAS']
final = [imgOriginal, img]
for i in xrange(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(final[i])
    plt.title(titles[i])
    plt.grid()
    plt.xticks([]), plt.yticks([])
plt.show()

cv2.imwrite('Hough_Lineas.jpg', img)

cd = cv2.waitKey(0)
cv2.destroyAllWindows()
