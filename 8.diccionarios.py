""" DICCIONARIOS
Estructura de datos que nos van a permitir almacenar diferentes tipos de datos, incluidos otros diccionarios

se diferencia de las listas y tuplas ya que no es por indices, sino claves, similar a los objetos en javascript

Las claves deben de ser tipos de datos inmutables como 
    - tuplas
    - numeros
    - strings

Si hay 2 claves iguales, se tomará la ultima clave con su valor (la que esté de ultima hacia abajo o hacia a la derecha si se esta escribiendo sin identación)  
"""
dictionary = {
    'name': 'jorge',
    5: 'soy un cinco',
    (1,2): [True, False],
    'tupla': ('x','y'),
    'a':10,
    'a': 100,
    1: {
        'last name': 'Munera'
    }
}
print(dictionary)


""" Agregar par clave - valor"""
dictionary['nueva clave'] = ['soy', 'una', 'nueva', 0]
print(dictionary)

""" Modificar el valor de una clave"""
dictionary['a'] = 200
print(dictionary)

""" Obtener datos de un diccionario"""
valor = dictionary['a'] #Me regresa el valor de la clave a, si la clave no existe regresa un error
print(valor)

""" Obtener datos de un diccionario con get('clave', 'tipo de dato a retornar ')"""
valor_2 = dictionary.get('z', [1,'string', False])
print(valor_2)

""" Eliminar un par clave-valor de un diccionario"""
del dictionary[5]
print(dictionary)

""" Obtener claves de un diccionario"""
claves = dictionary.keys() 
print('no es la lista pura en si:',claves)
print('lista pura:', list (dictionary.keys()))

""" Obtener valores de un diccionario"""
values = dictionary.values() 
print('no es la lista pura en si:',values)
print('lista pura:', list (dictionary.values()))

""" Obtener claves o valores en tuplas
Para esto, aplica lo mismo que las listas, solamente que indicamos que queremos una tupla"""
print('tupla pura:', tuple (dictionary.values()))

""" Fusionar 2 diccionarios"""
""" Forma 1"""
dictionary_2 = {'y': 'soy y', 'z': 'soy z'}
dictionary['y'] = dictionary_2['y']
dictionary['z'] = dictionary_2['z']
print('Fusion de diccionarios 1:',dictionary)

"""Forma 2"""
dictionary.update(dictionary_2)
print('Fusion de diccionarios 2:', dictionary)
