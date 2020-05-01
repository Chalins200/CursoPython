''' 2.- Modifique el método anterior para convertirlo 
en una propiedad (@property).
'''

class Punto:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	@property
	def cuadrante(self):
		mensaje = ""
		if self.x < 0 and self.y > 0:
			mensaje = "Pertenecen al cuadrante verde (-,+)."
		elif self.x > 0 and self.y > 0:
			mensaje = "Pertenecen al cuadrante naranja (+,+)."
		elif self.x < 0 and self.y < 0:
			mensaje = "Pertenecen al cuadrante rojo (-,-)."
		elif self.x > 0 and self.y < 0:
			mensaje = "Pertenecen al cuadrante azul (+,-)."

		return mensaje

p = Punto(-2,6)
print("Las coordenadas ", p.x, ",", p.y, p.cuadrante)

