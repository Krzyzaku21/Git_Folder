#dziedziczenie klas
# %%
from classes import Car
# ? Inheritanced class ElectricCar from Car
class ElectricCar(Car): #klasa dziedziczona Car z pliku classes.py
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #przekazanie atrybutów klasy Car
        self.battery_size = 75
        self.charge_level = 0
# ? Indyvidual function inheritance charge
    def charge(self):
        self.charge_level = 100
        print("the vehicle fully charged")
# ? Overriding method class Car
    def fill_tank(self):
        print("This car is not for gas but electric")
my_electric_car = ElectricCar('Tesla', 'Models', 2019)
my_electric_car.charge()
my_electric_car.drive() #funkcja dziedziczona z classes Car
my_electric_car.fill_tank() #This car is not for gas but electric
#the vehicle fully charged
#the car is moving
# %%
class Dog():
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(f" You can sit {self.name}.")

class SarDog(Dog):
    def __init__(self, name):
        super().__init__(name)

    def search(self):
        print(f"{self.name} is searching")

first_dog = SarDog("Wille")
print(f"{first_dog.name} is a search dog") # Wille is a search dog
first_dog.sit() # You can sit Wille.
first_dog.search() # Wille is searching

# %% dziedziczenie z klasy Animal po klasach Cat i Dog
#superclass Animal, subclass Cat, Dog
class Animal:
  def __init__(self, name, color):
    self.name = name
    self.color = color
class Cat(Animal):
  def purr(self):
    print("Purr...")
class Dog(Animal):
  def bark(self):
    print("Woof!")
fido = Dog("Fido", "brown")
print(fido.color) #brown
fido.bark() #Woof!
mruk = Cat("Burek", "red")
print(mruk.color) #red
mruk.purr() #Purr...
# %% superclass Wolf, subclass Dog
class Wolf: 
  def __init__(self, name, color):
    self.name = name
    self.color = color
  def bark(self):
    print("Grr...")
class Dog(Wolf):
  def bark(self):
    print("Woof")
husky = Dog("Max", "grey")
husky.bark() #Woof
# %% dziedziczenie miedzy klasami
class A:
  def method(self):
    print("A method")
class B(A):
  def another_method(self):
    print("B method")
class C(B):
  def third_method(self):
    print("C method")
c = C() #klasa C zawiera w sobie to co w klasie A i B
c.method() #A method
c.another_method() #B method
c.third_method() #C method
# %% super - funkcja do odwoływania się w klasie podrzędnej
# do klasy nadrzędnej
class A:
  def spam(self):
    print(1) #1, spam klasy A
class B(A):
  def spam(self):
    print(2) #2, spam klasy B
    super().spam() #odwołanie do metody spam w klasie A
B().spam()# 2, 1 #wywołanie def spam klasy B z
# zawartoscia super().spam() metody A
# %%
class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def show(self):
    print(f"i am {self.name} and i am {self.age} years old")
  def speak(self):
    print("bla bla")
class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color
  def speak(self):
    print("Meow")
  def show(self):
    print(f"i am {self.name} and i am {self.age} years old and i am {self.color}")
class Dog(Pet):
  def speak(self):
    print("Bark")
p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 2, "red")
c.show()
d = Dog("Burry", 7)
d.speak()


# %%

