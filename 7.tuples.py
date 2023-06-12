""" TUPLAS
Son un tipo de dato que nos van a permitir almacenar diferentes tipos de datos
A diferencia de las listas no puede ser modificada, es inmutable

Siempre que necesitemos tener un control total sobre ciertos datos y no vayan a mutar en todo el proyecto, podemos utilizar tuplas

ejemplo: un servidor donde voy a utilizar datos que no van a cambiar, passwords, permisos, rutas"""

my_tuple = (1, 'string', True)
print(my_tuple)
print(my_tuple[0:2]) # Aplican todos los metodos de listas