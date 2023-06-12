""" LIST - COMPREHENSION
es un feature que nos permite crear listas, tuplas y diccionarios de una forma sencilla

reglas para lista:
    1. valor a agregar a la lista
    2. un ciclo
    3. podemos tener condicionales internos
"""

""" LISTAS """
"""crear una lista sin comprehension"""
lista = []
for item in range(0, 101) :
    lista.append(item)
print('sin comprehension', lista)


""" crear lista con comprehension"""
lista_2 = [item for item in range(0,101) ]
print('LISTA - comprehension', lista_2)

""" crear lista con comprehension y condicional interno"""
lista_3 = [item for item in range(2, 101) if item % 2 == 0]
print('LISTA - comprehension', lista_3) # lista con numeros pares


""" TUPLAS """
""" crear tupla con comprehension y condicional interno"""
lista_4 = tuple (item for item in range(2, 101) if item % 2 != 0) # necesitamos colocar la clase de tuple
print('TUPLA - comprehension', lista_4) # lista con numeros impares


""" DICCIONARIOS """
""" crear diccionario con comprehension y condicional interno"""
diccionario = { indice: valor for indice, valor in enumerate(lista) if indice <= 20}
print('DICTIONARY - comprehension', diccionario)