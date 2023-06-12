""" CONDICIONALES

Python no trabaja con llaves para los ciclos
para que python sepa que bloque de codigo le va a pertenecer a algun if, un ciclo o una clase, debemos identar

if condicion :
    codigo
elif condicion:
    codigo
else:
    codigo

operadores logicos:
    = (asignacion)
    == (comparacion)
    != (diferente)
    > (mayor)
    < (menor)
    >= (mayor o igual)
    <= (menor o igual)
    and (y)
    or (o)

consideraciones:
    True = 1
    False = 1
    None : es para indicar que una variable no tiene valor
    toda variable null o vacia será ([], (), {}, 0, '', None) = False
    toda variable con algun valor o tipo de valor = True

anotaciones:
    pass : nos permite continuar la lectura sin bloquear la app, por ejemplo, si ocurre x condicion pero no quiero o no se en el momento que hacer si pasa esa condicion, para que no bloquee entonces pass
"""

fruta = 'manzana'
if fruta == 'kiwi' :
    print('son iguales')
elif fruta == 'manzana' :
    print('es una manzana')
elif fruta == 'condicional n' :
    pass 
else:
    print('no son iguales')


""" Otra manera de escribir la misma condicional ejemplo
este lo utilizamos normalmente si es un valor u otro, pero cuando necesitamos tener en cuenta varias condicionales es mejor la inicial"""
mensaje = 'son iguales' if fruta == 'kiwi' else 'no son iguales'
print('manera compacta:', mensaje)





