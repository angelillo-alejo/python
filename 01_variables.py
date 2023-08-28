# VARIABLES
# todo en minuscula y snake case

my_string_variable = 'oli'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables
print(my_bool_variable, my_int_variable, my_string_variable)
print('Este es el valor de:',my_bool_variable)

# convertir de int a string
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#Funciones del sistema
print (len(my_string_variable))

#Variables en una sola linea
name, surname, alias, age ='Brais', 'Moure','MoureDev', 35
print(name, surname, alias, age, '.Mi edad es:', age, '.y mi alias es:')#Aunque se pueda hacer, no es de las mejores practicas.

#Inputs
first_name = input('Cual es tu nomnbre?')
age = input('Cual es tu edad')

print(first_name)
print(age)

#Forzamos el tipo
address: str = 'Mi direccion'
address = 32
print(type(address))










