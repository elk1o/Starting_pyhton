# -*- coding: utf-8 -*-


class Person():
    name = ""
    surname = ""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        pass


class Student(Person):
    __student_id = ""
    signatures = ""

    def __init__(self, name, surname):
        student_count = 0
        self.name = name
        self.surname = surname
        self.__student_id = student_count
        student_count += 1

class Teacher(Person):
    __teacher_id = ""
    signature = ""

    def __init__(self, name, surname,signature):
        teacher_count = 0
        self.name = name
        self.surname = surname
        self.signature = signature
        self.__student_id = teacher_count
        teacher_count += 1


class Classroom():
    name = ""
    students = []

    def __init__(self, name):
        self.name = name
        for i in range(1, 15):
            student_aux = Student('Name%d' % i, 'Surname%d' % i)
            self.students.append(student_aux)

    def getter(self):
        print("-------------------------------------------")
        print('Classroom %s' % self.name)
        for student in self.students:
            print('Name: %s - Surname: %s ' % (student.name, student.surname))
        print("-------------------------------------------")
        return


    def __str__(self): #Cuando llamas a un objeto le das un 'alias' así
        return self.name


class Subject():
    name = ""
    hours = ""
    __subject_id = ""

    def __init__(self, name, hours):
        subjects_count = 0
        self.name = name
        self.hours = hours
        self.__subject_id = subjects_count
        subjects_count += 1


class School():
    name = ""
    school_id = 375

    def __init__(self, name):
        self.name = name


classroom = Classroom('1ºB')
#For print attributes from an object(class), print(object.__dict__) but only attributes intialized
#print(classroom.__dict__)
classroom.getter()
