import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('min 2.png')
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
flag, binarizado = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binarizado',binarizado)

x = []
y = []
Sx = 0
Sy = 0
Sxx = 0
Sxy = 0
xx = 0
Pen = 0
cont = 0

[m, n] = binarizado.shape
bina = binarizado
print ' n    x    y     x*y    x*x'
print '----------------------------'
for i in range(m):
    for j in range(n):
        if bina[i, j] == 0:
            cont = cont + 1 
            x.append(i)
            y.append(j)
            Sx += i
            Sy += j
            xy = i * j
            Sxy = xy + Sxy
            xx = i * i
            Sxx = xx + Sxx
            print '',cont,'  ', i,'  ', j,'  ',xy,'  ',xx
print ''
print 'Sumatoria X = ', Sx,'Sumatoria Y =', Sy
Pen = (Sxy - (float(Sx*Sy)/cont)) / (Sxx - (float(Sx*Sx)/cont))

Sx = float(Sx)/cont
Sy = float(Sy)/cont
print ''
print 'X media: ', Sx, '|| Y media: ', Sy
b = Sy - Pen * Sx
print ''
print 'Pendiente: ', Pen , 'Ordenada al Origen: b = ', b
print 'Ecuación de la recta'
print 'y = (',Pen,')*x +', b

a = np.arange(0,m,0.1)
fx = Pen * a + b

plt.grid(True)
plt.plot(x, y,'rx')
plt.hold(True)
plt.plot(a, fx, 'b')
plt.show()

