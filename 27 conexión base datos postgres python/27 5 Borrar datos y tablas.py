import psycopg2

conexion = psycopg2.connect(database = "Vision", user = "postgres",
                password = "system", host = "127.0.0.1", port = "5432")

print "Conectado a Base de Datos 'Visión' "

cursor = conexion.cursor()

## borrar registros:

cursor.execute("DELETE FROM USUARIO2;")

print "Registros borrados exitósamente"

## borrar tablas:

cursor.execute("DROP TABLE USUARIO2")

print "Tabla Usuario2 borrada"

conexion.commit()
conexion.close()
