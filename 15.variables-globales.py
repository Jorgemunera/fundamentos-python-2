"""" VARIABLES GLOBALES 
Aplican las mismas reglas del scoope de las funciones

Nota:
    - podemos cambiar el valor de una variable global dentro del scope de bloque de una funcion con la palabra reservada global y seguido el nombre de variable
        global variable

    - podemos crear variables globales dentro de funciones
    
"""

def palindromo(oracion):
    oracion = oracion.replace(' ', '').lower()
    if oracion == oracion[::-1]:
        return True
    else:
        return False

frase = 'Anita lava la tina'
resultado = palindromo(frase)
print('is palindromo:',resultado)


""" CAMBIAR VALOR DE UNA VARIABLE GLOBAL"""
print('valor global inicial:',frase)
def valor_global():
    global frase
    frase = 'pepito esta enfermito'
    return frase

print('valor global cambiado desde una funcion:',valor_global())


""" CREAR UNA VARIABLE GLOBAL DENTRO DE UNA FUNCION """
def crear_global():
    global nueva_variable
    nueva_variable = 'esto es una variable global nueva'
crear_global() # la ejecutamos para que la cree
print(nueva_variable) # ya la podemos acceder desde afuera de la funcion