import sqlite3, cvs

class DB(object):
	"""docstring for DB"""
	def __init__(self, nombre):
		self.nombre = nombre

	def abrir(self, nombre):
		conexion = sqlite3.connect(self.nombre,'.sqlite3')
		return conexion


	def createTable(self, tabla, campos):
		conexion = abrir(self.nombre)
		cursor = conexion.cursor()
		cursor.execute('CREATE TABLE if not exists ', tabla, '(', campos, ')')
		cerrar(cursor,conexion)


	def Consultar(self, tabla, campos, filtro):
		conexion = abrir(self.nombre)
		cursor = conexion.cursor()
		if filtros != '':
			cursor.execute('SELECT ', campos, ' FROM ', tabla, ' WHERE ', filtros)
			registros = cursor.fetchall()
		else:
			cursor.execute('SELECT ', campos, ' FROM ', tabla)
			registros = cursor.fetchall()
		cerrar(cursor,conexion)
		return registros


	def cerrar(self, curso, conexion):
		curso.close()
		conexion.close()
		

	def Insertar(archivo, tabla):
		conexion = abrir(self.nombre)
		with open(archivo) as f:
			cf = cvs.DictREader(f, delimiter = ';')
			data = []
			for fila in cf:
				data.append(fila)
			cursor.executemany('INSERT INTO ', tabla, ' VALUES(', data[0], ')', data)

		conexion.commit()