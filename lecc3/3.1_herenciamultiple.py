# -*- coding: utf-8 -*-

class A(object):
    def __init__(self):
        print("a")
        #Llamada a constructor padre
        super(A,self).__init__()
        pass


class B(A):
    def __init__(self):
        print("b")
        #Llamada a constructor padre
        super(B, self).__init__()
        pass


class C(A):
    def __init__(self):
        print("c")
        super(C, self).__init__()
        pass


class Z(object):
    def __init__(self):
        print("z")
        super(Z, self).__init__()
        pass


class D(C, B, Z):
    def __init__(self):
        print("D")
        super(D, self).__init__()
        pass


""" Body """
print("__mro__:", [x.__name__ for x in D.__mro__])
instance = D()
print('\a')  #Beep--