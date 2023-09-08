### SETS ##

# El módulo sets proporciona clases para construir y manipular colecciones desordenadas de elementos únicos.

my_set = set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set)) #Inicialmente esto es un diccionario

my_other_set = {'Brais', 'Moure', 41} #Metemos datos y ya es un set
print(type(my_other_set))

print(len(my_other_set))
my_other_set.add('Jordi ENP')

#Un set no es una estructura ordenada y la forma de guardar elementos es desordenada
print(my_other_set)

print('Moure' in my_other_set)
print('Holi' in my_other_set)

my_other_set.remove('Moure')
print(my_other_set)

my_other_set.clear() #Borra todos los elementos
print(my_other_set)




