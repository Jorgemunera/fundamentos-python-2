""" VARIABLES DE CLASE 
son variables globales que tinen las clases y a las cuales podemos tener acceso cuando las requiramos

como saber cuando es una variable de clase o de instancia
    - instancia.__dict__ (esto nos muestra un diccionario con los atributos de la clase sin las variables de clase)

se pueden usar tambien dentro de la clase
si es una variable de clase se pueden cambiar desde fuera de la clase, por convencion podemos colocar a la variable de clase un _variable para que los otros devs entiendan que no se debe modificar
"""

class Circulo:
    pi = 3.1416
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.radio * self.radio * self.pi # 1ra forma de acceder a las variables de clase

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

print(circulo_uno.pi)
print(circulo_dos.pi)

""" variables de clase """
print(Circulo.pi) # 2da forma de acceder a las variables de clase
