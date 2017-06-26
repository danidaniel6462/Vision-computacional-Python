import cv2
import numpy as np

# definimos CannyThreshold
def CannyThreshold(lowThreshold):
    # Aplicamos un desenfoque gaussiano de 3x3
    # para eliminar el ruido de alta frecuencia en la imagen y la guardamos en
    # la variable detected_edges
    detected_edges = cv2.GaussianBlur(gray,(3,3),0)

    #Aplicamos Canny que recibe como parámetros
    # canny  (imagen con menos ruido,umbral bajo, umbralBajo*relación, tamaño del kernel)
    detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)

    # guardamos canny en una máscara para poder mostrarlo posteriormente
    dst = cv2.bitwise_and(img,img,mask = detected_edges) # just add some colours to edges from original image.
    #mostramos la máscara de Canny
    cv2.imshow('canny demo',dst)


#inicializamos el umbral bajo, máx_umbral Bajo, la relación, y el
# el tamaño del kernel respectivamente
lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3

# cargamos una imagen x
img = cv2.imread('comedian.jpg')
# La convertimos a escala de Gris
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# nombramos a nuestra ventana
cv2.namedWindow('canny demo')

#creamos una barra de valores para el umbral bajo hasta nuestro máx_umbral
cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)

CannyThreshold(0) # iniciamos el algoritmo
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
