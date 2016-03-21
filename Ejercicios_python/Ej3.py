# -*- coding: utf-8 -*-
import time
import random

#3)Crear la siguiente estructura de clases :
# Clase animal
# - método menú
# -opciones: salir, Perro, Gato y León las opciones perro y gato van con un tiempo de
# espera al terminar de 3 segundos, mientras que la opción león pide una tecla para
# continuar.
# Clase Domestico hereda de Animal
# -métodos perro y gato
# Clase Leon hereda de animal
# -métodos presa, velocidad, tiempo y mostrarMensaje.
# mostrarMensaje mostrará los mensajes de los tres métiodos anteriores a la vez

class Animal():
    def __init__(self):
        return

    def menu(self):
        print('-------Choose option: --------')
        option = input('1: Dog - 2: Cat - 3: Lion -- Q: Quit \n')
        while option != 'Q' and option != 'q':
            if option == '1':
                print("Wait 3 seconds please.")
                time.sleep(3)
            elif option == '2':
                print("Wait 3 seconds please.")
                time.sleep(3)
            elif option == '3':
                input('Press any key to continue..')
            print('-------Choose option: --------')
            option = input('1: Dog - 2: Cat - 3: Lion -- Q: Quit \n')
            print(option)
        return

class Domestico(Animal):
    def __init__(self):
        return

    def perro(self):
        return

    def gato(self):
        return

class Leon(Animal):
    def __init__(self):
        return

    def presa(self):
        preys = ['Gazelle', 'Wildebeest', 'Elephant', 'Crocodile']
        return preys[random.randrange(0,4)]

    def velocidad(self):
        speed = ['45km/h', '33km/h', '60km/h', '50km/h']
        return speed[random.randrange(0,4)]

    def tiempo(self):
        time = ['60','40','125','30']
        return time[random.randrange(0,4)]

    def mostrarMensaje(self):
        print("")
        print("------------------------------------------------------------------------------------------------")
        print( "Lion is hunting {} with a speed of {} in {} seconds".format( self.presa(), self.velocidad(), self.tiempo()) )
        print("------------------------------------------------------------------------------------------------")
        return

an = Animal()
an.menu()

leon = Leon()
leon.mostrarMensaje()