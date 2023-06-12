course = 'Curso'
my_string = 'Código facilito'

"""podemos comentar asi tambien"""

""" METODOS DE FORMATO"""

result = '{} de {}'.format(course, my_string) # Concatenamos con el metodo format
print(result)

result_2 = '{b} de {a}'.format(a = course, b = my_string) # Concatenamos con format, pero damos alias para elegir en que posicion va cada variable
print(result_2)

print(result.lower()) # Regresa todo el string a minuscula
print('lower no muta la variable result:',result)

print(result.upper()) # Regresa todo el string en mayuscula
print('upper no muta la variable result:',result)

print(result.title()) # Regresa el string con formato de title (las iniciales de cada palabra en mayus)
print('upper no muta la variable result:',result)


"""METODOS DE BUSQUEDA"""

pos = result.find('Có') # Regresa la posicion del primer match que encuentre, #regresa -1 si no encuentra coincidencia
print('posicion:',pos)

count = result.count('C') # Regresa la cuenta de lo que buscamos, distingue mayus y minus
print('contar caracter que cumpla condicion:', count)

new_string = result.replace('o', 'O') # Reemplaza en un string la condicion inicial por un parametro nuevo que queramos
print('replace', new_string )
print('no muta el string original:', result)

string_split = result.split(' ') # Separa un string  por el parametro que indiquemos
print(string_split)