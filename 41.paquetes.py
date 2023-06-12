""" PAQUETES
- es una carpeta que va a contener los modulos que nosotros necesitemos
- los modulos no son mas que archivos con extension .py los cuales al momento de ser llamados van a generar un binario
- no los podemos tener dispersos, hay que tenerlos agrupados por contexto
- al agruparlos vamos a tener un paquete, este siempre debe tener un archivo __init__.py
- con nuestro paquete y nuestro init, creamos nuestros modulos
- para poder hacer uso del paquete necesitamos colocar from nombre_paquete.modulo import funcion_o_lo_que_sea que necesitemos del modulo
- cuando mandamos a llamar el modulo, se creara un nuevo folder dentro del paquete y dentro habra otro init y otro modulo
- tambien podemos llamar al modulo o las funcionalidades configurando el __init__.py adecuadamente, de esa manera solo debemos tequerirlo por el nombre del paquete padre import la funcionalidad o clase o lo que sea que requiramos importar, este en el paquete o subpaquete que este
"""

# from paquete.gato import Gato
from paquete_animals import Gato
from paquete_animals import creador_gatos
from paquete_animals import CONSTANTE
from paquete_animals import perro

gato = creador_gatos('Michi')
print(gato.nombre)

print(CONSTANTE)

perro.comer()

gato.comer()