'''11.- Convierta el atributo “estado” de la clase Guerrero 
a una propiedad para que no pueda setearse a “defensa” cuando “estado_escudo” sea 0. 
En tal caso, deberá elevar una excepción ValueError, 
al igual que si el estado que quiere asignarse no es “defensa” o “ataque”.
'''

class Guerrero:
    """docstring for Guerrero"""
    def __init__(self):
        self.vidao = 100
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
        Guerrero.vida -= 20
        self.estado_arma -= 2


'''g2 = Guerrero()
g2.estado_escudo = 0
g2.estado = "defensa"
'''
g1 = Guerrero()
g1.estado = "correr"
