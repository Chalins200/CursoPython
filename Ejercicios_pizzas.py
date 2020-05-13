''' 1.- Importe namedtuple y utilizando la misma, 
cree una clase Pizza con los atributos tamanyo, 
precio e ingredientes. Luego, cree una lista vacía pizzas.
'''

import collections
from collections import Counter
from collections import defaultdict

Pizza = collections.namedtuple("_Pizza", "tamanyo, precio, ingredientes")

pizzas = []

''' 2.- Dada la lista “pedidos”, agruéguela al código, recorra la misma, 
cree instancias de la clase Pizza y agregue las mismas a la lista “pizzas”.
'''

pedidos = [
    ["XL", 100, ["Queso", "Jamón"]],
    ["XL", 120, ["Queso", "Pepperoni"]],
    ["M", 80, ["Queso", "Piña"]],
    ["S", 60, ["Queso"]],
    ["M", 70, ["Pepperoni"]],
    ["L", 90, ["Queso", "Pepperoni"]],
    ["L", 80, ["Queso", "Tomates"]],
]

for p in pedidos:
  print(p)

p1 = Pizza("XL", 100, ["Queso", "Jamón"])
p2 = Pizza("XL", 120, ["Queso", "Pepperoni"])
p3 = Pizza("M", 80, ["Queso", "Piña"])
p4 = Pizza("S",100,["Queso"])
p5 = Pizza("M", 70, ["Pepperoni"])
p6 = Pizza("L", 90, ["Queso", "Pepperoni"])
p7 = Pizza("L", 80, ["Queso", "Tomates"])

pizzas.append(p1)
pizzas.append(p2)
pizzas.append(p3)
pizzas.append(p4)
pizzas.append(p5)
pizzas.append(p6)
pizzas.append(p7)

for p in pizzas:
  print(p)


''' 3.- Utilizando collections.Counter, cree un objeto ranking_ingredientes 
que contenga todos los ingredientes de las instancias en la lista “pizzas” 
(incluyendo repetidos). Luego imprima el ingrediente más utilizado con la 
cantidad de pedidos que incluyeron el mismo.
** La impresión debe devolver [(‘Queso’, 6)]
'''

ranking_ingredientes = ["Queso", "Jamón","Queso", "Pepperoni","Queso", "Piña"
                        "Queso","Pepperoni","Queso", "Pepperoni","Queso", "Tomates"]

count = Counter(ranking_ingredientes)

print(count)


'''4.- Utilizando collections.defaultdict, cree un objeto con el tipo int por defecto. 
Luego, actualice el objeto con los valores de la variable 
ranking_ingredientes del paso anterior. Para finalizar, imprima el valor de las claves 
“Pepperoni” y “Pepinillos”; deben devolver 3 y 0 respectivamente.
'''

dic = defaultdict(int)



