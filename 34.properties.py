""" PROPERTIES 
properties que podemos utilizar en las clases de python
vamos a modificar el password y modificarlo a traves de los properties, property no es mas que un decorador

"""

class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password)
        self.email = email

    def __generar_password (self, password):
        return password.upper()
    
    @property # con esto podremos modificar nuestro atributo privado 
    def password(self):
        return self.__password
    
    # Vamos a poder modificar los atributos privados con las properties y los setters
    @password.setter
    def password(self, new_password):
        self.__password = self.__generar_password(new_password)
    
jorge = Usuario('jorge', 'jorge123', 'jorge@mail.com')
print(jorge.password) # aqui obtenemos el password en mayuscula y se debe a que mi funcion password la estoy convirtiendo en una propiedad
jorge.password = 'nuevo password' # y vemos un error en consola ya que no podemos modificar este atributo
print(jorge.password) # vamos a poder ver que el password lo pudimos modificar
