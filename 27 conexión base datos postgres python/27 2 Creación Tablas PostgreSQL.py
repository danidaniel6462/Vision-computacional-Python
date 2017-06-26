import psycopg2

conexion = psycopg2.connect(database = "Vision", user = "postgres",
                password = "system", host = "127.0.0.1", port = "5432")

print "Conectado a Base de Datos 'Visi�n' "

## creamos una variable cursos que nos permitir� realizar todas las instrucciones SQL

cursor = conexion.cursor()

## Aplicamos un m�todo del objeto cursor
## de esta manera creamos una tabla en la BDD VISI�N

cursor.execute('''CREATE TABLE RECONOCIMIENTO
       (ID              INT     NOT NULL,
       LETRA	        TEXT    NOT NULL);''')

##cursor.execute('''CREATE TABLE PRUEBA
##       (ID_PRUEBA       INT     NOT NULL,
##       NOMBRE_PRUEBA    TEXT    NOT NULL);''')

print "Tablas creadas exit�samente"

## Realizamos todas las ejecuciones en la conexi�n actual
conexion.commit()
## Salimos de la conexi�n de la BDD
conexion.close()
