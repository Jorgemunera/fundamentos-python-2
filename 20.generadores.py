""" GENERADORES 
Nos van a servir para poder crear objetos sin necesidad de almacenarlos en memoria ram, algunos ejemplos que ya habiamos visto:
    - enumerate()
    - range()
Siempre que queramos un generador vamos a utilizar la palabra reservada yield
"""
def generador(*args):
    print(args)
    for item in args:
        yield item * 10, item / 10, True # YIELD lo que va hacer tomar el valor y regresar para la posterior iteracion, no esta restringido a solo un valor, podemos regresar mas de uno
    
for valor1, valor2, valor3 in generador(1,2,3,4,5,6,6):
    print('- valor1:',valor1, '- valor2:', valor2, '- valor3:', valor3)