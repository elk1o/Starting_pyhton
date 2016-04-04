'''

Escribir un algoritmo que, para una suma de dinero dada, indique

cómo descomponerla en billetes y monedas corrientes. Se desea utilizar el

mínimo de billetes y monedas. No hay ninguna limitación respecto al número de

billetes y monedas disponibles.

'''

# -*- coding: utf-8 -*-
import sys, os, time, webbrowser, re
cents = 0.0
monedas = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
monedero = []
cant = input(u"Insert payment amount: ")
cant = cant.split('.')
try:
    cents = float('0.'+cant[1])
except:
    cents = 0.0

euros = int(cant[0])
contador = 0
contadorBilletes = 0
unidades = 0
resto = 0

for x in monedas:
    unidades, resto = divmod(euros, x)
    if unidades != 0:
        monedero.append((x,unidades))
        euros = resto

if cents > 0:
    for x in monedas:
        unidades, resto = divmod(cents, x)
        if unidades != 0:
            monedero.append((x, int(unidades)))
            cents = round(resto, 2)

monedero_final = "--------Cambio:---------\n"
for x in monedero:
    monedero_final += "----{}x{}€ \n".format(x[1],x[0])

monedero_final += "------------------------"
print(monedero_final)

cadena=""
for x in monedero:
    if x[0] >= 5: cadena += "%d billetes/s de %d euros" % (x[1],x[0])
    if x[0] < 5: cadena += "%d moneda/s de %s euros" % (x[1],x[0])
    cadena += '\n'
print(cadena)