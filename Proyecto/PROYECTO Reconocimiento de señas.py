'''                     UNIVERSIDAD CENTRAL DEL ECUADOR


                                LOZA    DANIEL
                                VEGA    THALÍA


                           ING. COMPUTACIÓN GRÁFICA


                      RECONOCIMIENTO DE LENGUAJE DE SIGNOS


                             VISIÓN COMPUTACIONAL
'''

# Importamos las librerías
import cv2
import numpy as np
import matplotlib.pyplot as plt
import psycopg2

# Captura de imagen
cap = cv2.VideoCapture(1)

while (cap.isOpened):
    _, frame = cap.read()
    
    Amin=18000
    Amax=20000
    Bmin=26000
    Bmax=29000
    
    # transformar captura de imagen de bgr a hsv
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
 
    # Color de piel minimo
    min = np.array([0,50,20],np.uint8)
    # Color de piel maximo
    max = np.array([20,128,255],np.uint8)

    # Umbral adecuado para el color de piel
    umbral = cv2.inRange(hsv,min,max)
    
    # Binarizamos la imagen
    flag, binarizado = cv2.threshold(umbral, 170, 255, cv2.THRESH_BINARY)

    # escribimos valores para dilatar y erosionar la imagen
    kernelD = np.ones((12, 12), np.uint8)
    kernelE = np.ones((3, 3), np.uint8)
    # dilatar imagen
    dilatacion = cv2.dilate(binarizado, kernelD, iterations = 1)

    # erosionar imagen
    
    erosion = cv2.erode(dilatacion, kernelE, iterations = 1)
    #cv2.imshow('erosion', erosion)

    # Generamos un cuadro negro para poder dibujar los contornos
    # drawing = np.zeros(binarizado.shape,np.uint8)

    # Aplicamos un desenfoque en la imagen
    desenfoque = cv2.medianBlur(erosion, 5)
    #edges = cv2.Canny(binarizado,0,100)

    # Contamos contornos en la imagen procesada
    contornos,hierarchy = cv2.findContours(desenfoque,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    conexion = psycopg2.connect(database = "Vision", user = "postgres",
                password = "system", host = "127.0.0.1", port = "5432")

    print "Conectado a Base de Datos 'Visión' "

    cursor = conexion.cursor()

    for i, cnt in enumerate(contornos):
        # Calculamos el área de los contornos
        # así despresiamos valores mínimos antes de graficar
        area = cv2.contourArea(cnt)
        if area > 10000:
            # dibujamos contornos en la imagen original
            cv2.drawContours(frame, contornos, i, (255, 0, 0), 3)

            # Utilizamos tipo de letra para la representación en pantalla
            font = cv2.FONT_HERSHEY_TRIPLEX
            
            # Condicionamos los valores para las letras
            # Letra A
            if area >= Amin and area <= Amax:
                cursor.execute('''SELECT LETRA FROM RECONOCIMIENTO WHERE ID = 11;''')
                filas = cursor.fetchall();
                for row in filas:
                    A = row[0]
                # Mostramos en pantalla la letra A obtenida de la base de datos
                cv2.putText(frame, A,(10,400), font, 3,(0,0,255),6)
            # Letra B
            if area >= Bmin and area <= Bmax:
                cursor.execute('''SELECT LETRA FROM RECONOCIMIENTO WHERE ID = 12;''')
                filas = cursor.fetchall();
                for row in filas:
                    variableBase = row[0]
                # Mostramos en pantalla la letra B obtenida de la base de datos
                cv2.putText(frame, variableBase,(10,400), font, 3,(222,0,255),6)
                # Utilizamos esta condición para valores mayores al de las letras
            # Letra C
            if area > 30000:
                cursor.execute('''SELECT LETRA FROM RECONOCIMIENTO WHERE ID = 13;''')
                filas = cursor.fetchall();
                for row in filas:
                    C = row[0]
                # Mostramos en pantalla la letra C obtenida de la base de datos
                cv2.putText(frame, C,(10,400), font, 3,(0,175,255),6)

    conexion.close()

    # Mostramos la imágen final con los contornos y las letras que corresponden
    cv2.imshow('Original', frame)

    # cerramos el programa
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
