import psycopg2

conexion = psycopg2.connect(database = "Vision", user = "postgres",
                password = "system", host = "127.0.0.1", port = "5432")

print "Conectado a Base de Datos 'Visión' "

## creamos una variable cursos que nos permitirá realizar todas las instrucciones SQL

cursor = conexion.cursor()

## Insertamos datos en la tabla creada anteriormente:

cursor.execute('''INSERT INTO USUARIO2 VALUES
        (111, 'DANIEL LOZA', 24, 'QUITUMBE BARRIO MULLULLACTA', 120.32);''')

cursor.execute('''INSERT INTO USUARIO2 VALUES
        (222, 'THALIA VEGA', 22, 'OTAVALITO' , 350.32);''')

cursor.execute('''INSERT INTO USUARIO2 VALUES
        (333, 'MICKEL LOZA', 11, 'SOLANDA', 500.12);''')

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
conexion.close()

print "Datos ingresados exitósamente"
