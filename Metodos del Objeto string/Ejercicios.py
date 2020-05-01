'''Metodos del Objeto string

1.- Dada la cadena “El veloz murciélago hindú comía feliz cardillo y kiwi”, 
imprimir su variante justificada a la derecha rellenando con ‘>’, 
a la izquierda rellenando con ‘<‘ y centrada en 60 caracteres con 
asteriscos utilizando métodos de cadenas.
'''
print("El veloz murciélago hindú comía feliz cardillo y kiwi".rjust(60, '>'))
print("El veloz murciélago hindú comía feliz cardillo y kiwi".ljust(60, '<'))
print("El veloz murciélago hindú comía feliz cardillo y kiwi".center(60, '*'))

'''
2.- Dada la cadena “Nuevo curso de Python 3”, utilizar los métodos de cadena e imprimir:
a) Su variante en mayúsculas
b) Su variante en minúsculas
c) Su variante intercambiando mayúsculas y minúsculas
d) Convertir el primer caracter de cada palabra a mayúscula
'''   
print("Nuevo curso de Python 3".upper())
 
print("Nuevo curso de Python 3".lower())
  
print("Nuevo curso de Python 3".swapcase())
    
print("Nuevo curso de Python 3".title())

''' 
3.- Utilizando métodos de cadenas, identificar cuál de las siguientes 
cadenas posee solo caracteres alfabéticos: “Python 3”, “Python3”, “Python3.8” 
'''
    
"Python 3".isalpha()
"Python3".isalpha()
"Python3.8".isalpha()

'''
4.- Utilizando métodos de cadenas, identificar cuál de los siguientes
caracteres son ascii: ñ, d, s, a, $, &.

Validar uno a uno con str.isascii()
'''
ñ.isascii() 
d.isascii()
s.isascii()
a.isascii()
$.isascii()
&.isascii() 


'''
5. Utilizando métodos de cadenas, crear una variable con una 
lista de números pares del 2 al 10 como cadenas e imprimir sus 
valores separados por un guión medio.
'''
pares = ['2','4','6','8','10']
print('-'.join(pares))


'''
6.- Del ejercicio anterior, guardar en una variable el valor 
impreso y volver a separar sus valores utilizando métodos de cadenas.
'''

cadena = '-'.join(pares)
print(cadena.split('-'))

''' 
7.- Dada una expresión matemática “2 * 15 = 30”, 
cambiar el asterisco por una “x” y el signo “=” por la cadena “es igual a” 
utilizando métodos de cadenas. 

**Puede que precises utilizar dos veces el mismo método.
'''
    
"2 * 15 = 30".replace("*", "x").replace("=", "es igual a")

'''
8.- Dada la expresión “{1} * {2} = {0}”.format(15, #, #), 
reemplaza los numerales para que la cadena sea una expresión válida.
'''
    
"{1} * {2} = {0}".format(15, 3, 5)

'''
9.- Codifica la cadena “El veloz murciélago hindú comía feliz cardillo y kiwi” 
a una secuencia de bytes con utf-16, guarda el valor en una variable 
y luego vuelve a decodificarla para imprimir la cadena. 
'''
  
codif = "El veloz murciélago hindú comía feliz cardillo y kiwi".encode('utf-16')
print(codif)
decodif = codif.decode('utf-16')
print(decodif)
