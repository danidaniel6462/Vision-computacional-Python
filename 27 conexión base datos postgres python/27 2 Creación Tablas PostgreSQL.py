import psycopg2

conexion = psycopg2.connect(database = "Vision", user = "postgres",
                password = "system", host = "127.0.0.1", port = "5432")

print "Conectado a Base de Datos 'Visión' "

## creamos una variable cursos que nos permitirá realizar todas las instrucciones SQL

cursor = conexion.cursor()

## Aplicamos un método del objeto cursor
## de esta manera creamos una tabla en la BDD VISIÓN

cursor.execute('''CREATE TABLE RECONOCIMIENTO
       (ID              INT     NOT NULL,
       LETRA	        TEXT    NOT NULL);''')

##cursor.execute('''CREATE TABLE PRUEBA
##       (ID_PRUEBA       INT     NOT NULL,
##       NOMBRE_PRUEBA    TEXT    NOT NULL);''')

print "Tablas creadas exitósamente"

## Realizamos todas las ejecuciones en la conexión actual
conexion.commit()
## Salimos de la conexión de la BDD
conexion.close()
