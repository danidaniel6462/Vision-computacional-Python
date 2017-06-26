import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('quick2.png')
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
flag, binarizado = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)
blur = cv2.GaussianBlur(gris, (5,5), 0)

thresh = 100
max_thresh = 255

x = []
y = []
a = []
cont = 0

[m, n] = binarizado.shape
bina = binarizado

for i in range(m):
    for j in range(n):
        if bina[i, j] == 0:
            x.append(i)
            y.append(j)
            a.append([[i, j]])
print a
b = np.array(a)
print 'arreglo', b

ax = min(x)
ay = y[0]
bx = max(x)
by = y[len(y)-1]

xs = [ax, bx]
ys = [ay, by]

plt.grid(True)
plt.plot(x, y, 'rx')
plt.hold(True)
plt.plot(xs, ys)
plt.show()


edges = cv2.Canny(blur, thresh, thresh*2)
drawing = np.zeros(img.shape, np.uint8)

contourns, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contourns:
    hull = cv2.convexHull(cnt)
    cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 2)
    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 2)
    cv2.imshow('output', drawing)
    cv2.imshow('input', img)

    
cv2.waitKey(0)
cv2.destroyAllWindows()

