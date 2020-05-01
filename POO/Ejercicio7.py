'''7.- Amplíe el funcionamiento del ejemplo anterior para que el ataque sea realizado únicamente si el atributo “estado_arma” de la clase que ejecuta el método es mayor o igual a 2.
'''

class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100


	@property
	def estado_arma(self):
		return self._estado_arma


	@estado_arma.setter
	def estado_arma(self, estado_arma):
		if estado_arma < 2:
			raise ValueError("No se puede generar el ataque. Estado del arma es ", estado_arma)
		self._estado_arma = estado_arma


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
