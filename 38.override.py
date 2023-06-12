""" OVERRIDE - Sobreescritura de metodos
primer ejecuta os metodos de la clase a la que pertenece, sino busca en la siguiente escala de herencia
"""

class Animal:
    @property
    def terrestre(self):
        return True

class Felino(Animal):
    @property
    def garras_retractiles(self):
        return True
    
    def cazar(self):
        print('el felino esta cazando')

class Mascota():
    def __init__(self, nombre ):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)


class Gato(Felino, Mascota):
    def __init__(self, nombre):
        Mascota.__init__(self, nombre)

    def gato_cazador(self):
        self.cazar()
    
    def mostrar_nombre(self): # sobreescritura de metodos
        Mascota.mostrar_nombre(self) # podemos llamar al metodo de la clase padre, pero llamandolo directamente con el nombre de la clase
        print('metodo de clase hija - el nombre del gato es : {}'.format(self.nombre))

gato = Gato('Paco') # notemos que nos marcara un error ya que nos va a pedir el nombre como argumento, y el __init__ no esta en Gato, esta en Mascota, asi que tambien se hereda esta necesidad de acuerdo a las propiedades definidas en el constructor padre
# aunque aqui pongamos el nombre para que no marque error, abajo es sobreescrito y por eso en consola igual se muestra michi
gato.nombre = 'Michi'
gato.mostrar_nombre()