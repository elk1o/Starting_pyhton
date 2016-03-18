# -*- coding: utf-8 -*-
from random import randint

class Jugador(object):
    nombre = ""
    dorsal = ""
    posicion = ""

    def __init__(self, nombre, dorsal, posicion):
        self.nombre = nombre
        self.dorsal = dorsal
        self.posicion = posicion


class Entrenador(object):
    nombre = "Eugenio Lumbreras"
    experiencia = "30 años"
    titulos = "0"


class Club():
    nombre = "Club de baloncesto Góbalo CB"
    #plantilla = [Jugador(nombre="Jugador %d" % n, dorsal=n, posicion=n) for n in range(1, 10)]
    #Att protegido
    _plantilla = []
    #Att privado (no accesible) . Técnica de renombrado de nombre
    __entrenador = Entrenador()
    director_deportivo = "Reprise"
    liga = "1ª DIV"
    #Para hacer publico el atributo jugador, habría que inicializarlo antes del contructor
    jugador = ""


    def __init__(self):
        for i in range(1,12):
            jugador = Jugador('Jugador%d' % i,i,'Puesto: %d' % randint(1,5))
            self._plantilla.append(jugador)

    def ficha_tecnica(self):
        print (" Datos equipo: \n Nombre: %s \n Entrenador: %s \n Director deportivo: %s \n Liga: %s" % \
              (self.nombre,self.__entrenador.nombre,self.director_deportivo,self.liga))
        print ("Jugadores:")
        for jug in self._plantilla:
            print (jug.nombre)

    def posiciones(self):
        for j in self._plantilla:
            print(j.posicion)

if __name__ == "__main__":
    et = Club()
    et.ficha_tecnica()
    et.posiciones()
    et.status = "estrella"
    print(et.status)