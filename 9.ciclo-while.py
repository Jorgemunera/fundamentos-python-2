""" WHILE 
estructura:
    while condicion:
        codigo
    else:
        codigo

anotaciones:
    continue (nos permite que el ciclo se siga ejecutando)
    break (interrumpe el ciclo de manera abrupta)

"""
contador = 0
while contador <= 10: 
    print(contador)
    contador = contador + 1
    # contador += 1
    if contador == 5 :
        continue
    if contador == 7 :
        break
else:
    print('el while a terminado')