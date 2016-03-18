# -*- coding: utf-8 -*-
semaforo = 'verde'
#semaforo = 'amarillo'
#semaforo = 'rojo'
#--------------------** IF-ELSE statment **------------------------

if semaforo == 'verde':
    print ('Cruzar la calle')
else:
    print ('Esperar')

#--------------------** IF-ELSEIF-ELSE statment **------------------------

if semaforo == 'verde':
    print ('Cruzar la calle')
elif semaforo == 'amarillo':
    print ('Correr')
else:
    print ('Esperar')

euros_monedero = 50
precio = 60

if precio > euros_monedero:
    print ('Necesita mas dinero')
else:
    print ('Aqui tiene su ticket')

#--------------------** WHILE statment **------------------------
mylist = ['Flor','Manuel','Roberto','Naomi','Ainara']
year = 2000
while year <= 2016:
    print ('Feliz año nuevo %d' % year)
    year += 1

while True:
 nombre = raw_input("Indique su nombre: ")
 if nombre:
     print ('Ok, thanks %s' % nombre)
     mylist.append(nombre)
     break

#--------------------** FOR statment **------------------------
for name in mylist:
    print (name)

for i in range(0,10):
    print (i)