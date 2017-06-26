import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

imgOriginal = cv2.imread('monedas.jpg', 0)
cv2.imshow('Imagen Original', imgOriginal)
img = cv2.imread('monedas.jpg', 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 0, maxRadius = 0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2) #circunferencia
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3) #centro del círculo

titles = ['ORIGINA', 'TRANSFORMADA DE HOUGH_CIRCULOS']
final = [imgOriginal, cimg]

for i in xrange(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(final[i])
    plt.title(titles[i])
    plt.grid()
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.imwrite('Hough_Círculos.jpg', img)

cd = cv2.waitKey(0)
cv2.destroyAllWindows()
