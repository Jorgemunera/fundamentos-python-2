""" FUNCIONES 
utilizaremos la palabra reservada "def" name_function (): y tabulacion

podemos utilizar pass para no hacer nada y continuar la app
"""

def factorial_numero (numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial

print(factorial_numero(5))