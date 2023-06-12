""" HERENCIA MULTIPLE 
una clase puede heredar de muchas clases, basta solo con colocar en el parentesis el nombre de las clases de las que hereda separadas por ,
"""

class Animal:
    @property
    def terrestre(self):
        return True

class Mascota:
    nombre = ''
    def mostrar_nombre(self):
        print(self.nombre)

class Felino(Animal):
    @property
    def garras_retractiles(self):
        return True
    
    def cazar(self):
        print('el felino esta cazando')   

class Gato(Felino, Mascota): # clase que hereda de multiples clases
    def gato_cazador(self):
        self.cazar()




gato = Gato()
gato.nombre = 'Michi'
print(gato.mostrar_nombre())