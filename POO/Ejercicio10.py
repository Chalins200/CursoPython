'''10.- Cree una nuevo atributo “estado_escudo” a la clase Guerrero, que se inicialice en 100 por defecto.
'''

class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100
		self.estado = "ataque"
		self.estado_escudo = 100


	@property
	def estado_arma(self):
		return self._estado_arma


	@estado_arma.setter
	def estado_arma(self, estado_arma):
		if estado_arma < 2:
			raise ValueError("No se puede generar el ataque. Estado del arma es ", estado_arma)
		self._estado_arma = estado_arma


	@property
	def is_alive(self):
		return "Vivo" if self.vida > 0 else "Muerto"


	def atacar(self, Guerrero):
		Guerrero.vida -= 20
		self.estado_arma -= 2


g1 = Guerrero()
g2 = Guerrero()
g2.estado = "defensa"
g1.atacar(g2)

print("Guerrero 1 Vida: ", g1.vida)
print("Guerrero 1 Arma: ", g1.estado_arma)
print("Guerrero 1 Esta: ", g1.is_alive)
print("Guerrero 1 Estado: ", g1.estado)
print("Guerrero 2 Vida: ", g2.vida)
print("Guerrero 2 Arma: ", g2.estado_arma)
print("Guerrero 2 Esta: ", g2.is_alive)
print("Guerrero 2 Estado: ", g2.estado)
