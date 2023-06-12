"""para poder manejar esta clase como una excepcion, debemos heredar de exception"""

class TinyIntError(Exception):
    def __init__(self):
        self.message = 'el numero no cuenta con las caracteristicas de un numero tinyInt'

    def __str__(self):
        return self.message