""" EXCEPCIONES (ERRORES)
una excepcion son los errores que se generan en nuestro script al momento que este se esta ejecutando
podemos manejarlos de manera correcta para que no bloquee nuestra app y crashee
"""

""" EJEMPLO 1"""
def division(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError as err:
        print('error:',err)
        print('no es posible dividir en cero')

division(5,0)
print('se terminó la division')


""" EJEMPLO 2 """
def print_item():
    try:
        lista = [1,2]
        print(lista[9])
    except Exception as err: # con exception podemos capturar ccualquier tipo de error que venga
        print('hubo un error:', err)
    finally: # siempre se va a ejecutar
        print('terminó funcion print item')

print_item()
