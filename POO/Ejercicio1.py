''' 1.- Cree una clase Punto que reciba las coordenadas (x, y) 
y un método que indique a qué cuadrante pertenece.
'''

class Punto:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def cuadrante(self):
		mensaje = ""
		if self.x < 0 and self.y > 0:
			mensaje = "Pertenece al cuadrante verde (-,+)."
		if self.x > 0 and self.y > 0:
			mensaje = "Pertenece al cuadrante naranja (+,+)."
		if self.x < 0 and self.y < 0:
			mensaje = "Pertenece al cuadrante rojo (-,-)."
		if self.x > 0 and self.y < 0:
			mensaje = "Pertenece al cuadrante azul (+,-)."

		return mensaje

p = Punto(2,6)
print(p.cuadrante())

