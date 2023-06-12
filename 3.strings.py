my_string = 'hola mundo \nsalto "aqui estoy"' # Salto delinea
print(my_string)

string_1 = 'soy string 1'
string_2 = 'soy string 2'

final_message_1 = string_1 + string_2 # Concatenar strings con +
print(final_message_1)

final_message_2 = "forma de concatenar #2: %s y %s" %(string_1, string_2) #Concatenar string con %s y %(variable1, variable2, ....) 
print(final_message_2)

final_message_3 = "forma de concatenar #3: {} y {}".format(string_1, string_2) # Concatenar con .format(variable1, variable2 ....)
print(final_message_3)
