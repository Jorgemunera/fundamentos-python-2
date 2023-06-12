""" FUNCIONES ANIDADAS 
funciones anidadas
clousers : funciones que retornan otras funciones
funciones que reciben como parametros otras funciones

"""
""" FUNCION ANIDADA """
def division(num1, num2):
    def validacion():
        return num1 > 0 and num2 > 0
    
    if validacion() : 
        return num1 / num2
    else :
        return print('no se puede realizar la division')
    
resultado = division (10, 0)
print('FUNCION ANIDADA: ',resultado)

""" CLOUSER """
def funcion_clouser (num1, num2):
    def validacion():
        print('se ejecuta validacion')
        return num1 > 0 and num2 > 0
    return validacion

nueva_funcion = funcion_clouser(10, -5)
print('CLOUSER:',nueva_funcion())

""" FUNCIONES QUE RECIBEN OTRAS FUNCIONES COMO PARAMETRO"""
def aplicar_funcion(func):
    resultado = func()
    print('FUNCION EJECUTADA APARTIR DE FUNCION PASADA COMO PARAMETRO A OTRA:',resultado)

nueva_funcion2 = funcion_clouser(10, 9)
aplicar_funcion(nueva_funcion2)