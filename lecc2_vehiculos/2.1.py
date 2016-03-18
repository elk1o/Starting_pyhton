# -*- coding: utf-8 -*-
import os
import sys

LIMPIAR = "clear" if sys.platform.startswith("linux") else "cls"


class Vehicle():
    piloted = False
    stopped = False

    def __init__(self):
        pass

    def havePassengers(self):
        pass

class LandVehicle(Vehicle):
    def __init__(self):
        pass

    def changeGear(self):
        pass

    def pressClaxon(self):
        pass


class AirVehicle(Vehicle):
    def __init__(self):
        pass

    def takeOff(self):
        pass

    def land(self):
        pass


class Helicopter(AirVehicle):
    def __init__(self, helices):
        self.helices = helices
        pass

    def helicesOn(self):
        print('%d Helices starting' % self.helices)
        return

    def helicesOff(self):
        print('%d Helices stopping' % self.helices)
        return


class Plane(AirVehicle):
    def __init__(self, n_engines):
        self.n_engines = n_engines
        pass

    def enginesOn(self):
        print('%d Engines starting' % self.n_engines)
        return

    def enginesOff(self):
        print('%d Engines stopping' % self.n_engines)
        return


class Car(LandVehicle):
    def __init__(self, car_type, color):
        self.car_type = car_type
        self.color = color
        return

    def openTrunk(self):
        message = 'Opening car trunk from '+self.car_type+' color:'+self.color
        print(message)
        return

    def openDoor(self):
        message = 'Opening door from '+self.car_type+' color:'+self.color
        print(message)
        return


class Motorbike(LandVehicle):
    def __init__(self, motorbike_type, cilynder):
        self.motorbike_type = motorbike_type
        self.cilynder = cilynder
        return

    def switchOnLights(self):
        message = 'Switching on lights from '+self.motorbike_type+' cilynder:'+str(self.cilynder)
        print(message)
        return

    def coupleSidecar(self):
        message = 'Coupling sidecar form '+self.motorbike_type+' color:'+str(self.cilynder)
        print(message)
        return


class Menu():

    def __init__(self):
        pass

    def hideMenu(self):
        pass

    def showMenu(self):
        op = 0
        cad = ''
        continuar = ''
        while op != 3:
            os.system('clear') #If you know the OS
            #LIMPIAR
            print("Vehicles system: \n")
            print("Option 1: Car - Option 2: Bike - Option 3: Quit")
            print("")
            cad = input("Select option \n")
            if cad.isdigit():
                op = int(cad)
                if op == 1:
                    objcoche.openTrunk()
                    objcoche.openDoor()
                    objcoche2.openTrunk()
                    objcoche2.openDoor()
                    continuar=input('Press any key to continue')
                if op == 2:
                    objmoto.switchOnLights()
                    objmoto.coupleSidecar()
                    objmoto2.switchOnLights()
                    objmoto2.coupleSidecar()
                    continuar=input('Press any key to continue')
                if op == 3:
                    os.system('exit')
        pass

objmenu = Menu()
objcoche = Car('Sport','red')
objcoche2 = Car('Family','yellow')
objmoto = Motorbike('Cross',125)
objmoto2 = Motorbike('Road',500)
objmenu.showMenu()