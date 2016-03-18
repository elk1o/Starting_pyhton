# -*- coding: utf-8 -*-
class Coche:
    """Constructor del objeto coche"""
    def __init__(self,neumaticos,numero_puertas,caballos,combustible):
        self.neumaticos = neumaticos
        self.numero_puertas = numero_puertas
        self.caballos = caballos
        self.combustible = combustible

    def repostar(self):
        if self.combustible == 'Diesel':
            print("Puede repostar Diesel o Diesel e+")
        else:
            print("Puede repostar Gasolina SP 95 o Gasolina SP 98")

def nuevoCoche(neumaticos,puertas,caballos,combustible):
    coche = Coche(neumaticos=neumaticos,numero_puertas=puertas,caballos=caballos,combustible=combustible)
    return coche


mi_cocheG = nuevoCoche('Michelín',4,60,'Gasolina')
mi_cocheG.repostar()

mi_cocheD = nuevoCoche('Michelín',4,60,'Diesel')
mi_cocheD.repostar()
