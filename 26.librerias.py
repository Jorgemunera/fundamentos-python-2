""" 
LIBRERIAS
modulos predefinidos de python
python viene con 3 librerias incluidas
    - random (para obtener valores aleatorios)
    - datetime (si necesitamos cuestiones con la hora)
    - sys (trabajar con opciones de nuestro sistemas)
    - time (nos permite manejar delays)

"""
"""RANDOM"""
""" escoger un numero aleatorio """
import random
valor = random.randint(0,10) # entero aleatorio entre 0 y 10 incluyendolos
print(valor)

""" escoger un item de una lista """
lista = [True, 'jorge', 29, (1,2)]
valor2 = random.choice(lista)
print(valor2)

""" desorganizar una lista """
print('antes:',lista)
random.shuffle(lista)
print('despues:',lista)


""" DATETIME """
import datetime
print(datetime.datetime.now())


""" SYS y time"""
import sys
import time
for i in range(101):
    time.sleep(0.7)
    num_barras = i
    barras = '/' * num_barras
    sys.stdout.write('/')
    sys.stdout.write('\r%d %% %s' % (i, barras)) # imprimir x cosa, en este caso una barra de progreso en consola sin usar print
    sys.stdout.flush() # para que se pueda visualizar 