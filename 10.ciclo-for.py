""" CICLO FOR
nos va a permitir iterar listas, strings, tuplas

anotaciones:
    range(inicio,fin, paso) : es una funcion que me genera un rango, puedo indicar el inicio y el fin de este o puedo dar un unico numero pero el asume su inicio en 0, y puedo dar los 3 parametros y el rango tendrá unos saltos, eje de 2 en 2

    enumerate (lista) : funcion que me genera un objeto enumerable, nos sirve para cuando necesitamos los indices de una lista

    len(lista) : funcion que me da el numero de elementos en una lista, similar a length en js

    items() : metodo de los diccionarios que nos regresa las claves y valores
"""

""" ejemplo 1"""
lista = [1,2,3,4,5,6,7,8,9,10]

for item in lista:
    pass

""" ejemplo 2"""
nuevo_range = range(0,15)

for item in nuevo_range: #aqui podriamos meter la funcion range directamente
    pass

""" ejemplo 3"""
for indice, item in enumerate (lista) :
    print(item, 'tiene el indice', indice) # notemos que podemos pasar mas de 2 argumntos a print
""" ejemplo 4 """
for item in range(0, len(lista)) :
    print('len', item)

""" ejemplo 5 """
dictionary = {
    'a': 10,
    'b': 20,
    'c': 50
}

for clave, valor in dictionary.items() :
    print('la clave:', clave, 'tiene el valor:', valor)
