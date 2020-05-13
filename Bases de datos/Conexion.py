import sqlite3, csv

#creamos conexion
conexion = sqlite3.connect('pacientes.sqlite3')
print(type(conexion))

''' Base de datos en memoria 
conexion2 = sqlite3.connect(':memory:')
print(type(conexion2))
'''

#creamos un cursor
cursor = conexion.cursor()
print(type(cursor))


''' 
**************************************
#cramos una tabla  ('if not exists' es para evitar una excepcion si la tabla ya esta creada )
cursor.execute('CREATE TABLE if not exists pacientes(id integer PRIMARY KEY, nombre text, apellido text, edad integer, diabetico text)')


#Insertar datos 
conexion = conexion = sqlite3.connect('pacientes.sqlite3')
cursor = conexion.cursor()

#abrimos el archivo en modo lectura con codificacion utf-8
with open('pacientes.txt') as f:

	#utilizamos el metodo DictReader del modulo csv.
	#El mismo nos devuelve un objeto DictReader que podemos iterarlo como a una lista
	cf = csv.DictReader(f, delimiter =';')

	#Recorremos todos los elementos devueltos por DictReader
	for fila in cf:
		print(fila)
		#Creamos una sentencia sql accediendo al valor de cada columna en cada una de las filas
		sql = f'INSERT INTO pacientes values({fila["id"]}, "{fila["apellido"]}", "{fila["nombre"]}", {fila["edad"]}, "{fila["diabetico"]}")'
		print(sql)

		#ejecutamos la sentencia sql
		cursor.execute(sql)


conexion.commit()

**************************************


**************************************
#Simplificar insertar datos
#creamos conexion
conexion = sqlite3.connect('pacientes.sqlite3')
 
#creamos un cursor
cursor = conexion.cursor()
 
#Creamos los valores
valores = (6, "Matias", "Ferreyra", 28, "No")
 
#Insertamos los valores
cursor.execute('INSERT INTO pacientes(id, nombre, apellido, edad, diabetico) VALUES(?, ?, ?, ?, ?)', valores)
 
#confirmamos los cambios
conexion.commit()
 
****************************************
'''

'''
****************************************
#obtenemos todos los registros y guardamos en registros
cursor.execute('SELECT * FROM pacientes')
registros = cursor.fetchall()

#recorremos e imprimimos todos los registros
[print(registros) for registros in registros]

****************************************
'''


'''
****************************************
#obtenemos únicamente los registros de diabéticos
cursor.execute('SELECT name from sqlite_master where type= "table"')
registros = cursor.fetchall()
 
#imprimimos los valores obtenidos
[print(registro) for registro in registros]
 
****************************************
'''


'''
****************************************
#eliminamos registros de id mayor o igual a 5
cursor.execute('DELETE FROM pacientes WHERE id >= 5')
 
#Imprimimos los registros que fueron afectados por la sentencia ejecutada
print("Registros afectados:", cursor.rowcount)
 
#Confirmamos los cambios
conexion.commit()
 
#obtenemos todos los registros y guardamos en registros
cursor.execute('SELECT * FROM pacientes')
registros = cursor.fetchall()
 
#recorremos e imprimimos todos los registros
[print(registro) for registro in registros]
 
*****************************************
'''


'''
*****************************************
#seteamos el campo diabetico = No para todas las edades menor a 50
cursor.execute('UPDATE pacientes SET diabetico = "No" WHERE edad <= 50')
 
#Imprimimos los registros que fueron afectados por la sentencia ejecutada
print("Registros afectados:", cursor.rowcount)
 
#Confirmamos los cambios
conexion.commit()
 
#obtenemos todos los registros y guardamos en registros
cursor.execute('SELECT * FROM pacientes')
registros = cursor.fetchall()
 
#recorremos e imprimimos todos los registros
[print(registro) for registro in registros]

********************************************
'''

'''
********************************************
#obtenemos únicamente los registros de diabéticos
cursor.execute('DROP TABLE if exists pacientes')
 
#obtenemos únicamente los registros de diabéticos
cursor.execute('SELECT name from sqlite_master where type= "table"')
registros = cursor.fetchall()
 
#imprimimos los valores obtenidos
[print(registro) for registro in registros]

********************************************
'''


#Creamos una tabla medicos con los campos id y apellido
cursor.execute('CREATE TABLE if not exists medicos(id integer PRIMARY KEY, apellido text)')
 
#Creamos una lista de datos. Cada elemento es una tupla de valores
data = [(1, "Rodriguez"), (2, "Pérez"), (3, "Álvarez"), (4, "Acevedo")]
 
#Insertamos los valores pasando la lista de valores
cursor.executemany("INSERT INTO medicos VALUES(?, ?)", data)
 
#confirmamos los cambios
conexion.commit()
 
#obtenemos únicamente los registros de diabéticos
cursor.execute('SELECT * FROM medicos')
registros = cursor.fetchall()
 
#imprimimos los valores obtenidos
[print(registro) for registro in registros]


#cerramos conexiones
cursor.close()
conexion.close()


