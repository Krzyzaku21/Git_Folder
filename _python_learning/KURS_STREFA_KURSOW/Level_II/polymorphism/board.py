from abc import ABC, abstractmethod

class DuckBehavior(ABC): #klasa abstrakcyjna, wspólne zachowania dla kaczki i kaczki zabawowej DuckBehavior
# ! definiujemy te metody aby sie bezpsrednio nie odwoływać do tych metod w DuckToy aby było czytelne dla programisty
    @abstractmethod
    def fly(self):
        print(' duck fly')

    @abstractmethod
    def say(self):
        print(' kwa kwa')

    @abstractmethod
    def go_to(self):
        print('move duck')

class Duck(DuckBehavior):

    def __init__(self, age, breed):
        self.age = age
        self.breed = breed

    def fly(self):
        super().fly()

    def say(self):
        super().say()

    def go_to(self):
        super().go_to()

class Toy:

    def __init__(self, material, color):
        self.material = material
        self.color = color

# ! dziedziczenie wielokrotne - czytelne dziedziczenie wartosci inicjalizera Toy i danych z DuckBehavior po której dziedziczy Duck
class DuckToy(Toy, DuckBehavior):

    def fly(self):
        super().fly()

    def say(self):
        super().say()

    def go_to(self):
        super().go_to()

class Cat():
    def go_to(self):
        super().go_to()
