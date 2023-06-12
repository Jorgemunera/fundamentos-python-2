""" INIT 
vamos a colocar todos los modulos que necesitemos importar de la siguiente manera
- hay que colocar un .nombre_modulo
- el . es para que el interprete de python busque en el mismo nivel el modulo con el nombre especificado
- no es necesario colocar la extension .py

- dentro de init podemos tener nuestra propia logica
- tambien si tenemos un subpaquete solamente en el __init__.py superior colocamos .subpaquete import y lo que necesitemos
"""

from .felinos import Gato
from .felinos import Leon
from .animal import Animal


CONSTANTE = 'esto es una constante'

def creador_gatos(nombre):
    return Gato(nombre)

perro = Animal()
