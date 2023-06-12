def sum (num1, num2):
    return num1 + num2
print('suma',sum(2,3))

def division ( num1, num2 ):
    return num1 / num2
print('division',division(num2 = 10, num1 = 100)) # Agregamos manualmente el valor de cada paramtro

def producto (num1, num2 = 1) :
    return num1 * num2
print('producto',producto(6)) # podemos agregar valores iniciales a los parametros

"""importante
similar a js con la destructuracion podemos hacer algo parecido en python para retornar varios valores de una funcion
"""

def multiples_valores():
    return 'jorge', 100, True, {'a': 'soy la a'}

name, saldo, activo, obj = multiples_valores()
print(name)

""" Asignar funciones a variables"""
mi_variable = division
print('asignando una funcion a una variable:',mi_variable(100, 10))


""" EJECUTAR FUNCIONES DENTRO DE FUNCIONES"""
def mostrar_resultado(funcion):
    print('funcion interna como parametro:', funcion(6, 8))

mostrar_resultado(mi_variable)
