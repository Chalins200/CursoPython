'''12.- Modifique el método “atacar” de la clase Guerrero para que, actúe de la siguiente manera:
a: Si el “estado” de la instancia recibida es “defensa”, disminuya el estado del escudo en 5.
b: Si el “estado” de la instancia recibida es “ataque”, disminuya el estado de la vida en 20.
c: En cualquiera de los casos, dismuya en 2 el estado del arma que ejecuta el método.
d: Compruebe que el estado de la instancia que ejecuta el método sea “ataque”.
e: El ataque sea realizado únicamente si la instancia recibida esta viva.
'''

class Guerrero:
    """docstring for Guerrero"""
    def __init__(self):
        self.vida = 100
        self.estado_arma = 100
        self.estado = "ataque"
        self.estado_escudo = 100

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self,estado):
        if estado == "defensa" or estado == "ataque":
            if estado == "defensa" and self.estado_escudo == 0:
                raise ValueError("No se puede cambiar el estado. Escudo = 0")
            pass
        else:
            raise ValueError("El estado no existe.")
        self._estado = estado

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

    def atacar(self,Guerrero):
        if self.estado == "ataque" and Guerrero.is_alive == "Vivo":
            if Guerrero.estado == "defensa":
                Guerrero.estado_escudo -= 5
            elif Guerrero.estado == "ataque":
                Guerrero.vida -= 20
            self.estado_arma -= 2
        elif self.estado == "defensa":
            print("No se puedo realizar el ataque, estas en estado defensa.")
        elif Guerrero.is_alive == "Muerto":
            print("No se puede realizar el ataque por que el otro guerrero esta muerto.")
            


g1 = Guerrero()
g2 = Guerrero()

g1.estado = "ataque"
g2.estado = "defensa"

g1.atacar(g2)

print("Guerrero 1")
print("Is_alive: ", g1.is_alive)
print("Vida: ", g1.vida)
print("Estado: ", g1.estado)
print("Escudo: ", g1.estado_escudo)
print("Arma: ", g1.estado_arma)
print("//////////////")
print("Guerrero 2")
print("Is_alive: ", g2.is_alive)
print("Vida: ", g2.vida)
print("Estado: ", g2.estado)
print("Escudo: ", g2.estado_escudo)
print("Arma: ", g2.estado_arma)

print("//////////////")
print("//////////////")


g1.estado = "defensa"
g1.vida = 0
g2.estado = "defensa"

g2.atacar(g1)

print("Guerrero 1")
print("Is_alive: ", g1.is_alive)
print("Vida: ", g1.vida)
print("Estado: ", g1.estado)
print("Escudo: ", g1.estado_escudo)
print("Arma: ", g1.estado_arma)
print("//////////////")
print("Guerrero 2")
print("Is_alive: ", g2.is_alive)
print("Vida: ", g2.vida)
print("Estado: ", g2.estado)
print("Escudo: ", g2.estado_escudo)
print("Arma: ", g2.estado_arma)