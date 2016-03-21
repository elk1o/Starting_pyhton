# -*- coding: utf-8 -*-

# 4) Crear una estructura de dos clases independientes sin clase madre con un método
# compartido con el fin de trabajar con el polimorfismo

class Football():
    name = "football"
    def __init__(self):
        return

    def play(self):
        print("Playing {}!".format(self.name))
        return

class Basketball():
    name = "basket"
    def __init__(self):
        return

    def play(self):
        print("Playing {}!".format(self.name))
        return


def play(sport):
    sport.play()

play(Football())
play(Basketball())