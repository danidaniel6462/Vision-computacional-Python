##      CONEXI�N A BASE DE DATOS

## Importamos la librer�a que nos permite la conexi�n entre los
## programas python y postgreSQL 

import psycopg2


conexion = psycopg2.connect(database = "Vision", user = "postgres",
                password = "system", host = "127.0.0.1", port = "5432")

print "Conectado a Base de Datos 'Visi�n' "
