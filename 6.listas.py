my_list = ['jorge', 29, True, 14.04]

""" Metodo Append('item')
Inserta un elemento al final de la lista"""
my_list.append(6)
print(my_list)

"""" Metodo Insert('posicion','new value')
Inserta un elemento en la lista
Recibe 2 parametros
    1. la posicion donde voy a insertar
    2. el valor que quiero agregar"""
my_list.insert(1, 'Alexander')
print(my_list)

""" Metodo remove
Elimina un elemento que coincida con la condicion"""
my_list.remove('jorge')
print(my_list)

""" Metodo pop()
Remueve el ultimo elemento de la lista
Es un metodo mutable"""
item_pop = my_list.pop()
print(item_pop)
print(my_list)

""" Metodo sort()
ordena listas de un mismo tipo de valor, string, number
Sin parametros: ordena la lista de acuerdo a ASCI ascendente
con parametro reverse = True: ordena descendente"""
list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
list_3 = ['diez', 'once']

list_1.sort()
print(list_1)

list_3.sort(reverse = True)
print(list_3)

""" Metodo extend
Sirve para unir dos listas
es un metodo mutable"""
list_1.extend(list_2)
print(list_1)

list_2.append(list_3) # Hay diferencia con append como vemos
print(list_2)

