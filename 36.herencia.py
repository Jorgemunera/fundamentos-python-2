""" HERENCIA 
herencia es un mecanismo de python que nos permitirá crear una clase a partir de clases ya existentes, todos los metodos y propiedades seran heredados por las clases hijos salvo que sean metodos privados"""

class Animal: # clase padre
    @property
    def terrestre(self):
        return True

class Felino(Animal): # clase que hereda de la padre
    @property
    def garras_retractiles(self):
        return True
    
    def cazar(self):
        print('el felino esta cazando')   

class Gato(Felino): # clase que hereda
    def gato_cazador(self):
        self.cazar()

class Jaguar(Felino): # clase que hereda
    pass



gato = Gato()
jaguar = Jaguar()

print(gato.gato_cazador())
print(jaguar.garras_retractiles)
print(jaguar.terrestre)
