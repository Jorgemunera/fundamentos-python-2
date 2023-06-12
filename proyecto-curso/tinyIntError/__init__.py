from .validates import validate_tiny_int, validate_value
from .error import TinyIntError

# validar que sea un numero y no un string
def tiny_int(numero, callback = None):
    try:
        if validate_value(numero) and validate_tiny_int(numero):
            return True
        else:
            raise TinyIntError()
    except TinyIntError as err:
        if callback != None:
            callback()
        else:
            print(err)

def callback_function():
    print('esto se ejecuta cuando existe un error')
