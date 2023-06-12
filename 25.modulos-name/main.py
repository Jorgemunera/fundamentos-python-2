""" MODULOS
el valor del atributo __name__ lo va a ser siempre __main__ cuando el script que este ejcutando sea el principal, cuando no es el del archivo principal que ejecutamos, tomará el nombre del archivo al modulo que pertenece

por eso solemos encontrar en codigos
if __name__ == '__main__':

"""
from calculadora import __name__ as __name__calculadora
print(__name__)
print(__name__calculadora)

