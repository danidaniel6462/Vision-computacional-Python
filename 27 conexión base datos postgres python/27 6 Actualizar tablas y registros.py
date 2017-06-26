import psycopg2

conexion = psycopg2.connect(database = "Vision", user = "postgres",
                password = "system", host = "127.0.0.1", port = "5432")

print "Conectado a Base de Datos 'Visión' "

cursor = conexion.cursor()

## Actualizar registros:

cursor.execute('''UPDATE PRUEBA SET NOMBRE_PRUEBA = 'Prueba_actualizada',
                ID_PRUEBA = '123'  WHERE ID_PRUEBA = '4';''')

print "\nRegistro actualizado exitósamente\n"

cursor.execute('''SELECT * FROM PRUEBA
                  ORDER BY ID_PRUEBA DESC''')
cont = 0
for fila in cursor:
    cont = cont + 1
    print cont, repr(fila)

conexion.commit()
conexion.close()
