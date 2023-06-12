""" METODOS DE CLASE
Los metodos de clase al igual que los metodos estaticos le pertnecen a la clase, es decir, podemos utilizar estos metodos sin la necesidad de crear objetos, algo asi como un factory method

cual es la diferencia entre un methodo estatico y un metodo de clase?
los metodos de clase pueden acceder a los atributos o a los metodos de las clases que estamos heredando
"""

class Animal:
    volador = True

class Cocodrilo(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

# para que este metodo sea de clase, hay que decorarlo (con @classmethod), al igual que los metodos estaticos y en los parametros le mandamos cls
    @classmethod
    def new(cls, nombre):
        cls.volador = False # en estos metodos podemos acceder a los atributos de las clases que esta heredando, es decir las padres
        return Cocodrilo(nombre)
    
lagartija = Cocodrilo.new('lagar')
print(lagartija.nombre)
print(lagartija.volador)
