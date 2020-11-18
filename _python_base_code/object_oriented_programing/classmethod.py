# Classmethod = funkcja związana z tą klasą i tylko z tą klasą.
# Użyj tego typu, gdy używasz wartości klasy, a nie instancji
# (na przykład używając klasy, która pobiera całkowitą liczbę
# instancji tej klasy utworzonych i przechowywanych w zmiennej klasy).
# Nie musisz tworzyć ani jednej instancji, aby z niej korzystać.
# %% Create class method using classmethod()
class Person:
    age = 25
    def printAge(cls):
        print('The age is:', cls.age)
# create printAge class method
Person.printAge = classmethod(Person.printAge)
Person.printAge()
# %% Create factory method using class method
from datetime import date
# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)
    def display(self):
        print(self.name + "'s age is: " + str(self.age))
person = Person('Adam', 19)
person.display()
person1 = Person.fromBirthYear('John',  1985)
person1.display()
# %% Correct instance creation in inheritance
from datetime import date
# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)
    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)
    def display(self):
        print(self.name + "'s age is: " + str(self.age))
class Man(Person):
    sex = 'Male'
man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))
man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))
print(man.display())
print(man1.display())
# %%
class Person:
    number_of_people = 0
    GRAVITY = -9.8
    def __init__(self, name):
        self.name = name
    @classmethod
    def number_of_people(cls):
        return cls.number_of_people()
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("Jill")
print(Person.number_of_people)
# %%
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def calculate_area(self):
    return self.width * self.height
  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)
square = Rectangle.new_square(5)
print(square.calculate_area())
# %%
