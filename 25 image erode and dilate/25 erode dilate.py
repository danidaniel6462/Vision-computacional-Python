import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('erosionnnn.png')
cv2.imshow('original', img)

kernel = np.ones(3)
kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(img, kernel)
dilation = cv2.dilate(img, kernel)
fig = plt.figure()

titulos = ['imagen original', 'Erosion', 'Dilatacion']
final = [img, erosion, dilation]

for i in xrange(3):
    plt.subplot(1, 3, i+1), plt.imshow(final[i], 'gray')
    plt.title(titulos[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
