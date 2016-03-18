# -------** Tuplas. Variables que almacena varios datos. NO SE PUEDEN REESCRIBIR LOS DATOS (inmutables) **------
mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)
print(mi_tupla)
# Obtener un dato concreto de una tupla
print(mi_tupla[3])
# Obtener un rango de datos de una tupla
print(mi_tupla[1:3])
# Obtener un dato de manera inversa
print(mi_tupla[-1])

# ---------** Listas. Variables que almacena varios datos. SE PUEDEN REESCRIBIR LOS DATOS **----------------
mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
print(mi_lista)
# Obtener un dato concreto de una tupla
print(mi_lista[3])
# Obtener un rango de datos de una tupla
print(mi_lista[1:3])
# Obtener un dato de manera inversa
print(mi_lista[-1])
# Asignar nuevos valores a los datos
mi_lista[3] = 'nuevo valor'
print(mi_lista)
# Add nuevo valor
mi_lista.append('Added value')
print(mi_lista)

# Otra forma de inicializar una lista de forma dinamica:
mi_lista_2 = ["Jugador%d" % n for n in range(1, 10)]
print(mi_lista_2)

# ------------------------------** Diccionarios. 'Listas' indexadas con claves   **------------------
mi_diccionario = {'coche': 'VW Polo',
                  'moto': 'Kawasaki',
                  'avion': 'Boeing 747',
                  'tren': 'AVE'
                  }

print(mi_diccionario)
print(mi_diccionario['moto'])
# Eliminar una entrada del diccionario
del (mi_diccionario['moto'])
print(mi_diccionario)
# Modificar valores
mi_diccionario['avion'] = 'Airbus 525'
print(mi_diccionario)
# Adding one more
mi_diccionario['autobus'] = 'Scania'
print(mi_diccionario)
