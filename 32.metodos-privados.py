"""" METODOS PRIVADOS 
Si queremos proteger los metodos y atributos para que no puedan ser modificados
para esto en los atributos o metodos colocamos un __ y ya el interprete de python sabrá que es un atributo privado
"""

class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password) # atributo privado
        self.email = email
    
    def __generar_password(self, password):
        return password.upper()

    def get_password(self):
        return self.__password

jorge = Usuario('jorge', 'pass123', 'jorge@mail.com')
# print(jorge.__password) aqui tendriamos error porque el metodo es privado, asi que usaremos un metodo de la clase para retornarlo, ya que aqui si se puede acceder o modificar
print(jorge.get_password())
