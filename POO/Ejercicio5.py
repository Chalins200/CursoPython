'''5.- En la clase Guerrero definida anteriormente, 
escriba un método atacar que reciba otra instancia y 
disminuya de la vida de la misma en 20.
**Considere el concepto “duck typing”.
'''

class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100


	def atacar(self, Guerrero):
		Guerrero.vida -= 20


g1 = Guerrero()
g2 = Guerrero()

g1.atacar(g2)

print("Guerrero 1 Vida: ", g1.vida)
print("Guerrero 1 Arma: ", g1.estado_arma)
print("Guerrero 2 Vida: ", g2.vida)
print("Guerrero 2 Arma: ", g2.estado_arma)
