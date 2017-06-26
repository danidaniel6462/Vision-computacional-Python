import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('erosionnnn.png')
cv2.imshow('Original', img)

kernel = np.ones(20)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

fig = plt.figure()

titulos = ['Original','apertura','cierre']
final = [img, opening, closing]

for i in xrange(3):
    plt.subplot(1, 3, i+1), plt.imshow(final[i], 'gray')
    plt.title(titulos[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
