'''6.- Modifique el método anterior para que, además de disminuir el atributo “vida” de la instancia recibida, disminuya en 2 el atributo “estado_arma” del objeto que ejecuta el método.
'''

class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100
	

	def atacar(self, Guerrero):
		Guerrero.vida -= 20
		self.estado_arma -= 2


g1 = Guerrero()
g2 = Guerrero()
g1.atacar(g2)

print("Guerrero 1 Vida: ", g1.vida)
print("Guerrero 1 Arma: ", g1.estado_arma)
print("Guerrero 2 Vida: ", g2.vida)
print("Guerrero 2 Arma: ", g2.estado_arma)
