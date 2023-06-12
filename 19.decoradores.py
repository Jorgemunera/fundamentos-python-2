""" DECORADORES 
nos va a permitir agregar mayor funcionalidad a una funcion en concreto
tengase A, B , C funciones
un decorador es una funcion(A) que recibe como parametro otra funcion (B) para poder crear (C)
"""
def decorador(is_valid = True):
    def _decorador(func): # A, B
            # podemos hacer algo antes con esa func
        def before_action():
            print('- vamos a ejecutar la funcion')

            # podemos hacer algo despues de ejecutada esa func
        def after_action():
            print('- se ejecutó la funcion')

        def nueva_funcion(*args, **kwargs): # agregamos * y ** para que haya flexibilidad con los parametros que vamos a recibir en las funciones
            print('- saber que tiene args y kwargs', args, kwargs)

            if is_valid :
                before_action()

            resultado = func(*args, **kwargs)

            after_action()
            return resultado
        
        return nueva_funcion # C
    return _decorador

@decorador() # aqui podemos asignar parametros que recibe el decorador
def saluda():
    print('hola mundo')
saluda()

@decorador()
def suma(num1, num2):
    return num1 + num2
resultado = suma(25, 45)
print(resultado)
