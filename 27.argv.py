""" ARGV
vamos a pasarle parametros a nuestros scripts
hasta ahora para correr un archivo escribimos py name.py

podemos pasarle unos parametros por defecto en la terminal antes de ejecutar nuestro archivo script, todo eso quedara almacenado en una lista en sys.argv
"""

import sys

if __name__ == '__main__':
    if len(sys.argv) == 1: 
        print('que tiene argv:', sys.argv)     
        print('es necesario colocar por lo menos un argumento')
    else:
        lista = [item for item in sys.argv]
        for item in lista:
            print(item, end='--') # el print por defecto tiene un salto de linea en consola, de esta manera agregamos el separador que queremos entre print y print
    