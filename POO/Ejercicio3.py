''' 3.- Cree una clase Vector que reciba 2 instancias 
de la clase Punto y devuelva el vector resultante. 
Deberá poseer 3 atributos:
a: será el punto 1.
b: será el punto 2
c: @property ab: será una tupla del vector resultante que 
indicará la diferencia (distancia) entre los puntos recibidos.
'''
from math import sqrt

class Punto:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def distancia(self, otroPunto):
		punto_X = self.x - otroPunto.x
		punto_Y = self.y - otroPunto.y

		return sqrt(punto_X ** 2 + punto_Y ** 2)

pA = Punto(2,6)
pB = Punto(3,5)

class Vector():
	def __init__(self, puntoA, puntoB):
		self.puntoA = puntoA
		self.puntoB = puntoB

	@property
	def distancia(self):
		return (Punto.distancia(self.puntoA,self.puntoB))


puntoA = Punto(2,3)
puntoB = Punto(5,5)

vec = Vector(puntoA, puntoB)


print("La distancia entre los puntos A y B es de : ", vec.distancia)
	 

