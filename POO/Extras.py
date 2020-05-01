''' Extras.
1.- Cree una nueva clase Arma que posea los atributos nombre, daño y estado. El atributo estado debe poseer las características del atributo estado_arma que definimos en la clase Guerrero.
2.- Cree una nueva clase Escudo que posea los atributos nombre, absorción y estado. El atributo estado debe poseer las mismas características del atributo estado_escudo de la clase Guerrero.
3.- Modifique la clase Guerrero para que ahora los atributos estado_arma y estado_escudo pasen a ser manejados por atributos arma y escudo que posean instancias de dichas clases.
4.- Modifique el método atacar y la property estado de la clase Guerrero para que considere los cambios realizados en el punto anterior.
5.- Modifique el método atacar para que en vez de disminuir en 20 la vida de la instancia recibida, considere el daño del arma que posee el objeto y la absorción del escudo respectivamente. El daño a la vida debe ser la diferencia entre ambos. En caso que el escudo posea mayor absorción que el arma, no se hará ningún daño a la vida de la instancia recibida pero se desgastará el arma del Guerrero que ataca.
'''
class Arma(object):
    """docstring for Arma"""
    def __init__(self):
        self.nombre = nombre
        self.dano = dano
        self.estado = 100

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        if estado < 2:
            raise ValueError("No se puede generar el ataque. Estado del arma es ", estado_arma)
        self._estado = estado


class Escudo(object):
    """docstring for Escudo"""
    def __init__(self):
        self.nombre = nombre
        self.absorcion = absorcion
        self.estado = 100
        

class Guerrero:
    """docstring for Guerrero"""
    def __init__(self, Arma, Escudo):
        self.vida = 100
        self.arma = Arma
        self.estado = "ataque"
        self.escudo = Escudo

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self,estado):
        if estado == "defensa" or estado == "ataque":
            if estado == "defensa" and self.escudo.estado == 0:
                raise ValueError("No se puede cambiar el estado. Escudo = 0")
            pass
        else:
            raise ValueError("El estado no existe.")
        self._estado = estado
    

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
            

