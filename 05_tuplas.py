### TUPLAS ###

"""Las tuplas son secuencias de elementos similares a las listas, la diferencia principal es que las tuplas no pueden ser modificadas directamente, es decir, una tupla no dispone de los métodos como append o insert que modifican los elementos de una lista."""

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, 'Brais', 'Moure')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Brais')) #Cuantos hay
print(my_tuple.index('Moure')) #Dice el indice
print()
