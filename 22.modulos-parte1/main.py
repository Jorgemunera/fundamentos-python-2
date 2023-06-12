""" MODULOS 
Cuando comenzamos a tener mucho codigo debemos modularizar nuestro codigo siguiendo el principio de una sola responsabilidad

cuando importamos un modulo de python se crea una carpeta llamada __pycache__ , alli se genera un archivo con extension .pyc que es un archivo compilado en nuestro modulo en caso no exista, esto lo hace porque los archivos compilados aumentan el performance de nuestra app, hace que sea mas rapido, esto lo hace para tomar los archivos compilados y no los interpretados
"""

import calculadora

resultado = calculadora.suma(30, 60)
print(resultado)