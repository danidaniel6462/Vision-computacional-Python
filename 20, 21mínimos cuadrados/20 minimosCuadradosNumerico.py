import numpy as np
import matplotlib.pyplot as plt
import cv2

##n = input('Ingrese el número de elementos: ')
n = 4
##x = np.random.randint(1, 15, n)
##y = np.random.randint(1, 15, n)
x = [1, 2, 4, 5]
y = [2, 4, 5, 7]

Sx = 0; Sy = 0; Sxx = 0; Sxy = 0; xx = 0; Pen = 0; cont = 0

print ' n    x    y     x*y    x*x'
print '----------------------------'
for i in range(n):
    cont = cont + 1 
    Sx += x[i]
    Sy += y[i]
    xy = x[i] * y[i]
    Sxy = xy + Sxy
    xx = x[i] * x[i]
    Sxx = xx + Sxx
    print '',cont,'  ', x[i],'  ', y[i],'  ',xy,'  ',xx
print ''
print 'Sumatoria X = ', Sx,'Sumatoria Y =', Sy
Pen = (Sxy - (float(Sx*Sy)/cont)) / (Sxx - (float(Sx*Sx)/cont))

Sx = float(Sx)/cont
Sy = float(Sy)/cont
print 'X media = ', Sx, '|| Y media = ', Sy
b = Sy - Pen * Sx
print 'Pendiente: ', Pen , 'Ordenada al Origen: b = ', b
print ''
print 'Ecuación de la recta'
print 'y = (',Pen,')*x +', b

a = np.arange(0,14,0.1)
fx = Pen * a + b

plt.grid(True)
plt.plot(x, y,'ko')
plt.hold(True)
plt.plot(a, fx, 'r')
plt.show()

