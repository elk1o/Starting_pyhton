# -*- coding: utf-8 -*-
import os
import sys
import csv
import time

#bloque 1  leer archivo datos.csv con reader y mostrar cada registro
# print(open('datos.csv'))
with open('datos.csv') as csv_file:
    fp = csv.reader(csv_file)
    print(fp)
    for x in fp:
        print(x)

print("------------------------------------")
time.sleep(2)

#bloque 2  leer el archivo csv y mostrar solo la cabecera y el primer registro sin bucles y sin with
# la segunda linea tiene que mostrarse sin corchetes ni comas ni comillas
fp = open('datos.csv')
data_fp = csv.reader(fp)
record = next(data_fp)
print(record)
'''
record = next(data_fp)
name = record[0]
prov = record[1]
cons = record[2]
'''
#Comprehension list
name, prov, cons = next(data_fp)
print("People: \n")
print("Name: {} - Province: {} - Consumption: {}".format(name,prov,cons))

del name, prov, cons , data_fp
fp.close()
del fp
print("------------------------------------")
#bloque3  leer el archivo y separarlo por comas cada registro y que parezcan los registros de forma lineal

superlist = []
fp = open('datos.csv')
data_fp = csv.reader(fp)
cont = 0
for i in data_fp:
    if(cont!=0):
        superlist.append(i)
    cont += 1
#Sort list ASC
superlist.sort()
print(superlist)
print(" DIalectos csv de las cabeceras de ficheros")
print(csv.list_dialects())

#BLoque 4 Escribir un fichero de salida de nombre salida.csv separado por |

fp = open('salida.csv', 'w')
for x in superlist:
    fp.write(str(x)+'\n')
fp.close()
os.system("subl salida.csv")