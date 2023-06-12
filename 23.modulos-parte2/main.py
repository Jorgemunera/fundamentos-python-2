""" MODULOS 
Esta es otra manera de importar modulos en python
podemos renombrar con la palabra reservada as
tambien podemos importar en lineas distintas de un mismo modulos
"""

from calculadora import suma, resta, division
from calculadora import producto as multiplicacion

resultado = suma(30, 60)
resultado2 = resta (50, 25)
resultado3 = multiplicacion (50, 25)
resultado4 = division (50, 25)
print('suma', resultado)
print('resta', resultado2)
print('producto', resultado3)
print('division', resultado4)


""" Otra forma de importar
con el * estamos indicando que importe todo, esta no es tan buena forma porque no es tan legible el hecho de que no sabemos que funcionalidades estamos importante
"""
# from calculadora import *