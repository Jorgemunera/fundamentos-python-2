""" METODOS ESTATICOS 

Los metodos que estan dentro de una clase con la palabra self, son metodos de instancia
los metodos que estan dentro de la clase y no tienen la palabra self, son metodos estaticos, pero hay que decorarlo con @staticmethod
"""

class Circulo:

    @staticmethod
    def pi():
        return 3.1416 

    def __init__(self, radio):
        self.radio = radio

    def area(self): # metodos de instancia
        return self.radio * self.radio * self.pi() # podemos acceder con self o con el nombre de la clase

circulo_uno = Circulo(4)

print(Circulo.pi()) # podemos acceder desde la clase
print(circulo_uno.area()) # podemos acceder desde el objeto