# vamos a crear una funcion que va a recibir un valor y retornara un verdadero o falso si el numero es tinyint
def validate_tiny_int(numero):
    return numero >= 0 and numero <= 255

# funcion que verifica si el numero es instancia de enteros int
def validate_value (numero):
    try:
        return isinstance(int(numero), int)
    except ValueError as err:
        return False