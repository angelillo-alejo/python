### TUPLAS ###

"""Las tuplas son secuencias de elementos similares a las listas, la diferencia principal es que las tuplas no pueden ser modificadas directamente, es decir, una tupla no dispone de los métodos como append o insert que modifican los elementos de una lista. 
LAS TUPLAS TIENEN PARENTESIS"""

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, 'Brais', 'Moure')
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Brais')) #Cuantos hay
print(my_tuple.index('Moure')) #Dice donde esta el indice de la palabra solicitada
print()

# my_tuple[1] = 1.80 ERROR, LAS TUPLAS SON INMUTABLES
# print (my_tuple)  ERROR, LAS TUPLAS SON INMUTABLES

my_sum_tuple = my_tuple + my_other_tuple
print (my_sum_tuple)
print(my_sum_tuple[3:6])

my_tuple =  list (my_tuple)
print (type(my_tuple))

my_tuple[3] = 'Brais'
my_tuple.insert(1, 'Blue')
print(tuple(my_tuple))