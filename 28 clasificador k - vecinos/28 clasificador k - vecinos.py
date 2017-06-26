import cv2
import numpy as np
import matplotlib.pyplot as plt

## creamos un arreglo lista1 para almacenar todos los datos para la clasificación
lista1 = []

## creamos datos aleatorios 
datos = np.random.randint(0,100,(25,2)).astype(np.float32)
## creamos datos aleatorios
responses = np.random.randint(0,2,(25,1)).astype(np.float32)

## representamos los datos de color rojo con un 0
## para mostrar como resultados en consola
rojo = datos[responses.ravel() == 0]
## ploteamos los datos de color rojo y con estrellas
plt.scatter(rojo[:,0],rojo[:,1],80,'r','*')

## representamos los datos de color azul con un 1
## para mostrar como resultados en consola
azul = datos[responses.ravel() == 1]
## ploteamos los datos de color azul y con estrellas
plt.scatter(azul[:,0],azul[:,1],80,'b','*')

## ploteamos los datos de color morado represetándolo con un rombo
morado = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(morado[:,0],morado[:,1],80,'m','D')

## utilizamos la función k-vecinos de OpenCV
knn = cv2.KNearest()
## utilizamos la función train, que recibe como parámetros
## los datos y respuestas
knn.train(datos,responses)

## utilizamos la función find_nearest
## para encontrar los vecinos más cercanos, en este caso seleccionamos 3
## vecinos, los más cercanos
ret, results, neighbours ,dist = knn.find_nearest(morado, 3)

## mostramos las distancias de cada uno de los vecinos más cercanos
print "Distancia: ", dist,"\n"
## Mostramos los vecinos más cercamos
## recordemos que estamos representando el azul con 1 y rojo con 0
print "Vecinos: ", neighbours,"\n"
## mostramos el resultado al cual va a pertenecer nuestra nuevo dato
print "Pertenece al grupo: ", results,"\n"

## incluimos el título a nuestra gráfica
plt.title("K - vecinos")
## ploteamos las diferentes etiquetas para los datos generados
plt.plot(lista1,marker = '*',color = 'r',linestyle = 'NONE',label = "Grupo rojo")
plt.plot(lista1,marker = '*',color = 'b',linestyle = 'NONE',label = "Grupo azul")
plt.plot(lista1,marker = 'D',color = 'm',linestyle = 'NONE',label = "vecino nuevo")
## ubicamos la leyenda o etiquetas en la parte superior de la gráfica
plt.legend(loc = "upper left")
## activamos la leyenda
plt.legend()
## presentamos la gráfica en pantalla
plt.show()
