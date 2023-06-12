""" ATRIBUTOS Y METODOS
ATRIBUTOS: caracteristicas seran atributos
METODOS: acciones que pueda realizar un objeto, dentro debemos indicar la palabra self
"""

class Lapiz:
    color = 'amarillo'
    contiene_borrador = False
    usa_grafito = True

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

lapiz_generico = Lapiz()
lapiz_generico.contiene_borrador = True
lapiz_generico.dibujar()
lapiz_generico.borrar()
