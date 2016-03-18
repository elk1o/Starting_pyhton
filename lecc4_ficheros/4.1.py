# -*- coding: utf-8 -*-
import os
import sys


class Menu:
    data = {}

    def __init__(self):
        pass

    def showMenu(self):
        option = ''
        cad = ''

        while option != 'Q':
            print("Temperatures system: \n")
            option = input("Option 1: Input temperature  - Option 2: Read list - Q: Quit  \n")
            print("")
            if (option == '1'):
                for x in range(0, 4):
                    city = input("Choose city\n")
                    temperature = input("Choose temperature\n")
                    print("Saving data ...")
                    # Salvar ciudad/temp en fichero
                    self.data[city] = temperature
                    print("-- Data saved --")
                self.createSave(self.data)

            if (option == '2'):
                self.readFile()

    def createSave(self, data):
        fp = open('grados.txt', 'a')
        register = ''
        for x, z in data.items():
            # format string
            register = "City = {0} , degreees= {1} ".format(x.upper(), z) + "\n"
            fp.write(register)
        fp.close()
        return

    def readFile(self):
        fp = open('grados.txt')
        for q in fp:
            print(q)
        fp.close()
        return
menu = Menu()
menu.showMenu()