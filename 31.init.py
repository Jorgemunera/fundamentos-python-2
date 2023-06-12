""" METODO INIT (similar al constructor de js)
Cuando nosotros necesitamos que nuestros objetos empiecen con unos valores establecidos utilizamos init
uso:
    def __init__(self):

    - a este init le podemos pasar los parametros que vamos a necesitar y en cada atributo anteponemos self.atributo = parametro
    - de igual manera como en cualquier funcion podemos establecer valores por default aqui en los parametros

"""

class Lapiz:
    def __init__(self, color = 'amarillo', contine_borrador = False, usa_grafito = False):
        self.color = color
        self.contiene_borrador = contine_borrador
        self.usa_grafito = usa_grafito

    def dibujar(self):
        print('el lapiz esta dibujando')

    def borrar(self):
        can_erase = self.can_erase()
        if can_erase:
            print('el lapiz esta borrando')
        else:
            print('no puede borrar')

    def can_erase(self):
        if self.contiene_borrador == True:
            return True
        else: 
            return False 

lapiz_generico = Lapiz('amarillo', True, False)
lapiz_generico.dibujar()
lapiz_generico.borrar()
