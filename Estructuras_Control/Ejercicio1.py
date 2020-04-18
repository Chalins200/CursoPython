'''Estructuras de control
1.- Dada una lista de valores numéricos, 
determine e imprima si la sumatoria de todos los 
valores excede a un valor máximo establecido en una variable.
'''
maximo = 30
valores = [20,5.8,6,15]
tmp = 0

for num in valores:
	tmp += num

if tmp > maximo:
	print("El valor excedel el maximo permitido.")