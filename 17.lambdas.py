""" LAMBDAS 
lambda nos sirve para poder crear pequeñas funciones anonimas en una sola linea de codigo
estas funciones anonimas nos van a servir mucho, las mandaremos a llamar dependiendo de las condiciones de nuestro programa

dentro de las lambdas no vamos a utilizar ciclos, ni condicionales
no hay necesidad de la palabra return ya que las lambdas retornan algo

si no regresan un valor, deben realizar una accion por ejemplo un print

uso:
    mi_variable = lambda num1, num2, numN: num1 + num2
"""
def sum(num1, num2):
    return num1 + num2

mi_funcion = sum # asignar funcion a una variable
resultado = mi_funcion(5, 10) # evaluar mi variable con los parametros que necesita la funcion
print('funcion normal:',resultado)

""" EJEMPLO LAMBDA 1 """
mi_funcion2 = lambda num1, num2 : num1 + num2
print('lambda:',mi_funcion2(5, 10))

""" EJEMPLO LAMBDA 2"""
formato = lambda sentencia : '{}???'.format(sentencia)
resultado2 = formato('puedes convertirme en pregunta')
print(resultado2)

""" EJEMPLO LAMBDA SIN VALOR """
no_valor = lambda : 10
resultado3 = no_valor()
print(resultado3)

""" EJEMPLO LAMBDA SIN VALOR Y SIN RESULTADO """
no_resultado = lambda : print('no retorno un valor como tal')
resultado4 = no_resultado()
print(resultado4)





