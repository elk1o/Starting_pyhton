class Pajaro():
    def __init__(self):
        pass

    def desplazar(self):
        print('Volando')
        return


class Cobra():
    def __init__(self):
        pass

    def desplazar(self):
        print('Reptando')
        return

#Función común


def mover(animal):
    animal.desplazar()


p = Pajaro()
c = Cobra()

p.desplazar()
c.desplazar()
mover(p)
mover(c)