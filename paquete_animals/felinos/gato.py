"""" podemos importar de carpetas de paquetes superiores con .."""

from ..animal import Animal

class Gato(Animal):
    def __init__(self, nombre):
        self.nombre = nombre