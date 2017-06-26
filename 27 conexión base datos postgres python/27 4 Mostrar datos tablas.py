import psycopg2

conexion = psycopg2.connect(database = "Vision", user = "postgres",
                password = "system", host = "127.0.0.1", port = "5432")

print "Conectado a Base de Datos 'Visión' "

cursor = conexion.cursor()

cursor.execute('''SELECT * FROM PRUEBA;''')

print "\nDatos ingresados en tabla Prueba: \n"

cont = 0
for fila in cursor:
    cont = cont + 1
    print repr(cont).rjust(2), repr(fila)

cursor.execute('''SELECT * FROM USUARIO2;''')

print "\nDatos ingresados en la tabla Usuario2\n"

filas = cursor.fetchall()

for row in filas:
    
    print repr(row[0]).rjust(4),
    print repr(row[1]).rjust(14),
    print repr(row[2]).rjust(4),
    print repr(row[3]).rjust(29),
    print repr(row[4]).rjust(6)


cursor.execute('''SELECT * FROM USUARIO2;''')
print "\ntabla Completa\n"

filas = cursor.fetchall();

for row in filas:
    cont = cont + 1
    print repr(cont).rjust(2), repr(fila)


conexion.close()

