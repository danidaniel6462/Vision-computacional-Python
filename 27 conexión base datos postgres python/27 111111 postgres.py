## importamos la librería necesaria para la conexión entre los programas python y postgreSQL

import psycopg2

##realizamos una conexión a la base de Datos creada

conexion = psycopg2.connect(database="Vision", user="postgres", password="system", host="127.0.0.1", port="5432")

print "Opened database successfully"

## creamos una variable cursos que nos permitirá realizar todas las instrucciones SQL

cursor = conexion.cursor()

## Aplicamos un método del objeto cursor
## de esta manera creamos una tabla en la BDD VISIÓN

##cursor.execute('''CREATE TABLE USUARIO2
##       (ID              INT     NOT NULL,
##       NOMBRE           TEXT    NOT NULL,
##       EDAD             INT     NOT NULL,
##       DIRECCION        VARCHAR(50),
##       SALARIO          REAL);''')
##
##cursor.execute('''CREATE TABLE PRUEBA
##       (ID_PRUEBA       INT     NOT NULL,
##       NOMBRE_PRUEBA    TEXT    NOT NULL);''')
##
print "Tabla creada exitósamente"
##
#### Realizamos todas las ejecuciones en la conexión actual
conexion.commit()
#### Salimos de la conexión de la BDD
##conexion.close()

## Insertamos datos en la tabla creada anteriormente:

##cursor.execute('''INSERT INTO USUARIO VALUES
##        (111, 'DANIEL LOZA', 24, 'QUITUMBE BARRIO MULLULLACTA', 120.32);''')
##
##cursor.execute('''INSERT INTO USUARIO VALUES
##        (222, 'THALIA VEGA', 22, 'OTAVALITO' , 350.32);''')
##
##cursor.execute('''INSERT INTO USUARIO VALUES
##        (333, 'MICKEL LOZA', 11, 'SOLANDA', 500.12);''')
cursor.execute('''INSERT INTO Prueba(
            id_prueba, nombre_prueba)
    VALUES (2, 'prueba2');''')
cursor.execute('''INSERT INTO Prueba(
            id_prueba, nombre_prueba)
    VALUES (3, 'prueba3');''')
cursor.execute('''INSERT INTO Prueba(
            id_prueba, nombre_prueba)
    VALUES (4, 'prueba4');''')
cursor.execute('''INSERT INTO Prueba(
            id_prueba, nombre_prueba)
    VALUES (5, 'prueba5');''')
cursor.execute('''insert into Prueba values (6, 'prueba6');''')
    
conexion.commit()

##print 'Datos ingresados exitósamente'

cursor.execute('''SELECT * FROM prueba;''')

print 'Datos ingresados: '

cont = 0
for fila in cursor:
    cont = cont + 1
    print cont, repr(fila)


cursor.execute("SELECT * from USUARIO2")

filas = cursor.fetchall()
for row in filas:
    
##   print "ID =        ", row[0]
##   print "NOMBRE =    ", row[1]
##   print "EDAD =      ", row[2]
##   print "DIRECCION = ", row[3]
##   print "SALARIO =   ", row[4], "\n"
    print repr(row)
##    print repr(row[0]).rjust(4),
##    print repr(row[1]).rjust(14),
##    print repr(row[2]).rjust(4),
##    print repr(row[3]).rjust(29),
##    print repr(row[4]).rjust(6)
   
print "Operaciones realizadas satisfactoriamente";

## borrar tablas:

'''cursor.execute("drop table Prueba")
conexion.commit()'''

## borrar registros
'''


cursor.execute("DELETE FROM USUARIO2")
cursor.execute("DELETE FROM PRUEBA")


cursor.execute("DELETE FROM prueba WHERE id_prueba = 3;")

de igual forma para editar o actualizar registros

 update usuarios set nombre='Marceloduarte', clave='Marce'
  where nombre='Marcelo';

actualizar nombre de tabla

ALTER TABLE PRUEBA RENAME TO TABLA_ACTALIZADA;

Cambiar el nombre a una columna:

ALTER TABLE TABLA_ACTALIZADA RENAME COLUMN nombre_actual TO nombre_nuevo

Borrar una columna

ALTER TABLE TABLA_ACTALIZADA DROP COLUMN nombre_columna

Agregar columna

ALTER TABLE TABLA_ACTALIZADA ADD COLUMN nombre_columna BOOLEAN DEFAULT true

Eliminarle a una columna la restriccion de no aceptar valores nulos

ALTER TABLE TABLA_ACTALIZADA ALTER COLUMN nombre_columna DROP NOT NULL

Modificar la columna para que apartir de ahora no acepte valores nulos

ALTER TABLE TABLA_ACTALIZADA ALTER COLUMN nombre_columna SET NOT NULL

Modificar el tipo de dato a una columna

ALTER TABLE TABLA_ACTALIZADA ALTER COLUMN nombre_columna TYPE smallint

Eliminar una Foreign-key constraint

ALTER TABLE TABLA_ACTALIZADA DROP CONSTRAINT nombre_foreign_key_fkey

Agregar una foreign-key

ALTER TABLE TABLA_ACTALIZADA ADD FOREIGN KEY(nombre_columna) REFERENCES nomina(nombre_columna)

Eliminar el valor que tiene por default una columna
'''


conexion.commit()
conexion.close()
