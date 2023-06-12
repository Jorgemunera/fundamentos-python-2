""" DOCSTRING 
FORMA 1
esto es generar la documentacion de las funciones del codigo que escribimos
- se debe colocar en la primer linea interna en la funcion, no antes

cuando hacemos esto el interprete de python entiende que esto es documentacion de la funcion, asi que lo podemos acceder como atributo de la funcion
documentacion = funcion.__doc__
"""

def generador(*args):
    """recibe n cantidad de numeros y regresa el numero ademas de regresar \nsi el numero es mayor a 5
    """
    for valor in args:
        yield valor, True if valor > 5 else False
    
nombre = generador.__name__
documentacion = generador.__doc__
print('__name__:',nombre)
print('__doc__:',documentacion)

""" FORMA 2 DE GENERAR DOCUMENTACIONES : INTERPRETE DE PYTHON
debemos entrar al interprete de python en la terminal, una vez alli importamos la funcion de la que queramos la documentacion"""
