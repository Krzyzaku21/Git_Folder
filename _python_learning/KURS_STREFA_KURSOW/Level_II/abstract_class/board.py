from abc import ABC, abstractmethod #klasa abstrakcyjna 2 sposób

class Animal(ABC):#klasa abstrakcyjna 2 sposób
    def __init__(self):
        raise Exception('Unable to create object of abstract class') #klasa abstrakcyjna

    def print_informacion(self):
        pass
    @abstractmethod #klasa abstrakcyjna 2 sposób
    def give_voice(self):
        raise NotImplementedError() #metody wirtualne

class Mammal(Animal):

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def go_to(self):
        print('go')

    def print_informacion(self):
        print(self.name)
        print(self.age)
        Animal.print_informacion(self)
        print('I am a mammal')

class Boy(Mammal):

    def __init__(self, age, name, surname):
        Mammal.__init__(self, age, name)
        self.surname = surname

    def give_voice(self): #nadpisanie metody
        print('Little boy want to play')

    def print_informacion(self):
        Mammal.print_informacion(self)
        print(self.surname)
        print('I am a boy')