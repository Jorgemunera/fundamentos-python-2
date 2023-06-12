""" ARGUMENTOS
anotacion adicional:
    para saber el tipo de dato que es una variable podemos usar la funcion type(variable)
"""
""" FUNCION CON N ARGUMENTOS QUE NO CONOZCO (*args)
si nosotros no conocemos la cantidad de argumentos que va a recibir nuestra funcion, podemos pasar con un * y el argumento para que el insterprete de python entienda y los convertirá en una tupla
def name_function(*args)

si no se pasa ningun argumento, devuelve una tupla vacia"""
def suma (*args):
    print(args) # para verlo que recibimos
    result = 0
    for item in args:
        result = result + item
    return result

resultado = suma(10,20,30,40,50)
print(resultado)


""" FUNCION CON ARGUMENTOS CON NOMBRES ESPECIFICOS QUE PUEDO TENER EN LA FUNCION (**kwargs)
tambien podemos darle un nombre especifico a cada uno de los argumentos que recibamos, para esto utilizamos def name_function(**kwargs), de tal manera que cuando invoque la funcion y la evalue debo especificar el nombre de las variables, el interprete de python cogera todo y nos devolverá un diccionario
"""
def resta(**kwargs):
    return kwargs

resultado_2 = resta(name = 'jorge', age = 30, activo = True)
print(resultado_2)