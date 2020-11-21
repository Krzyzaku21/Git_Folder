class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_informacion(self):
        print(self.age)
        print(self.name)

    def give_voice(self):
        print('Voice')

class Mammal(Animal):

    def __init__(self, age, name):
        Animal.__init__(self, age, name)

    def go_to(self):
        print('go')

    def print_informacion(self):
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