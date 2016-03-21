# -*- coding: utf-8 -*-

# 2) Crear una lista de nombres y a continuación solicitar el número de items a mostrar de
# la lista, con la validación de no introducir un número superior a los elementos de la # lista.

names = ['Alberto', 'Francisco', 'Sergio', 'Jorge', 'Jesús', 'David']

print('---** Selecting number of names **---')
index = 1
n_names = int( input(' How much names to display? \n') )
if(n_names <= len(names)):
    for x in range( n_names ):
        cad = 'Name {}: {} \n'.format(index, names[x])
        index += 1
        print(cad)
else:
    print("List haven't so much names. Displaying all list ...")
    for x in names:
        cad = 'Name {}: {} \n'.format(index, x)
        index += 1
        print(cad)

