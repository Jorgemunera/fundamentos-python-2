""" CLASES - PARTE FINAL 
como podemos cambiar el comportamiento de clases y objetos
"""
class Usuario:
    atributo = 'soy atributo'
    def __init__(self):
        self.__password = 'secreto'

    def mostrar_password(self):
        print(self.__password)

usuario = Usuario()
usuario.nombre = 'jorge'
usuario.apellido = 'munera' # podemos crear atributos que no esten definidos en la clase de esta manera

print(usuario.nombre)
print(usuario.__dict__) # aqui vamos a ver el atributo privado

usuario.__password = 'nuevo secreto'
print(usuario.__dict__) # y aqui vamos a ver un atributo nuevo publico __password

usuario.mostrar_password()


""" METODOS MAGICOS  IMPORTANTEEEE
estos empiezan por __ y terminan con __
ejemplo:
 __init__ :nos va permitir inicializar atributos y ejecutar metodos importantes pero no es el      constructor

 __new__ : este es el verdadero constructor de la clase y es el primer metodo que se ejecuta cuando se crea un objeto
    - no recibe a self como parametro sino a cls
    - necesita retornar super().__new__(cls), de esta manera se ejecuta el constructor y sigue con la ejecucion del __init__, si no estuviera el return no veriamos la salida del __init__

__str__ : este metodo me muestra un texto con la ubicacion del espacio en memoria de algun atributo o metodo de una clase, tambien debe retornar algo y debe ser string

__getattribute__: con este metodo podemos modificar la accion que se ejecute cuando se trate de acceder al atributo de un objeto que no existe, recibe 2 parametros, self y el nombre del atributo

"""

class Persona:
    def __new__(cls): # este no recibe a self sino a la cls
        print('este metodo se ejecuta primero')
        return super().__new__(cls)
    
    def __init__(self):
        print('este metodo se ejecuta segundo')

    def __str__(self):
        return 'modifique el __str__ y ahora se ejecuta esto'
    
    def __getattribute__(self, atributo):
        print('no se encontro el atributo {}'.format(atributo))

persona = Persona()
print(persona) # vemos el espacio en memoria de dicho objeto, cuando sobreescriba el metodo __str__ ya no vere eso sino que se ejecuta lo que yo indique

print(persona.lugar_nacimiento) # si se ejecuta esto asi solo, nos mostrara un error, puesto que el atributo no existe, pero si utilizamos el metodo __getattribute__ podemos modificar la accion cuando se trate de acceder a un atributo que no existe

