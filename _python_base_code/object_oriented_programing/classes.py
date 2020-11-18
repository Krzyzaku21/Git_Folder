# Klasy - indywidualne opisywanie wartosci i obiektów w klasie
# Metoda = funkcja związana z tym wystąpieniem klasy.
# Użyj tego typu, gdy używasz wartości własnej instancji
# (jej własnej nazwy, wieku itp.). Aby go używać, musisz utworzyć
# jedną instancję.
# %%
class Car:
    def __init__(self, make ,model, year):
        "Initialize car atrybutes"
        self.make = make
        self.model = model
        self.year = year

        #Fuel capacity and level in galleons:
        self.fuel_capacity = 60
        self.fuel_level = 0

    def fill_tank(self):
        "Fill gas tank to capacity"
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full")

    def drive(self):
        "Simulate driving"
        print("the car is moving")

    def update_fuel_level(self, new_level):
        "Update the fuel level"
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("the tank cant hold that much")

    def add_fuel(self, amount):
        "Add fuel to tank"
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("added fuel")
        else:
            print("the tank won't hold that much")

# ? Create object from a class
my_car = Car('audi', 'a4', 2016)
# ? Accessing attribute values
print(my_car.make, my_car.model, my_car.year) #audi a4 2016
# ? Calling methods
my_car.fill_tank() #Fuel tank is full
my_car.drive() #the car is moving
# ? Crating multiple objects
my_new_car = Car('subaru', 'outback', 2020)
my_new_car.fuel_level = 5
my_new_car.update_fuel_level(30)
print(my_new_car.fuel_level) #30
my_new_car.add_fuel(20) #added fuel
print(my_new_car.fuel_level, my_new_car.fuel_capacity) #50 60

# %%
# ? instances as atributes
class Battery:
    def __init__(self, size=75):
        self.size = size
        self.charge_level = 0

    def get_range(self):
        if self.size == 75:
            return 260
        elif self.size == 100:
            return 315

class ElectricCar1(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
# ? class Battery like instance of object battery
        self.battery = Battery() #instance like a class Battery

    def charge(self):
        self.battery.charge_level = 100
        print("The vehicle a fully charged")

my_ecar = ElectricCar1('tesla', 'model_x', 2019)
my_ecar.charge() #The vehicle a fully charged
print(my_ecar.battery.get_range()) #260
my_ecar.drive() #the car is moving

# %%
# ? operactions and make objects from class Car, ElectricCar
from inheritance import ElectricCar
"Make list to hold a fleet of cars"
gas_fleet = []
electric_fleet = []

"Make 500 gas cars and 250 electric cars"
for _ in range(500):
    car1 = Car('ford', 'escape', 2019)
    gas_fleet.append(car1)
for _ in range(250):
    ecar1 = ElectricCar('nissan', 'leaf', 2019)
    electric_fleet.append(ecar1)

# fill gas cars and charge electric cars
for car1 in gas_fleet:
    car1.fill_tank()
for ecar1 in electric_fleet:
    ecar1.charge()
print(f'gas cars: {len(gas_fleet)}') #500
print(f'Electric cars: {len(electric_fleet)}') #250
print(electric_fleet) # list of object class
# %%
class Dog():
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(f" You can sit {self.name}.")
first_dog = Dog("Fido")
print(f"{first_dog.name} is great name") # Fido is great name
first_dog.sit() # You can sit Fido.
# %%
class Cat:
    def __init__(self, color, legs): #wywołuje sie automatycznie, self pierwsy parametr
        self.color = color
        self.legs = legs
felix = Cat("white", 4)
rover = Cat("brown", 4)
print(felix.color, rover.color)
# %% odwoływanie do innych definicji w klasie
class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color
  def bark(self):
    print("Woof!")
fido = Dog("Fido", "brown")
print(fido.name) #Fido
fido.bark() #Woof!
# %%
class Dog: #klasa Dog
  legs = 4 #atrybut legs może być odwoływany do instancji klasy i samej klasy
  def __init__(self, name, color):
    self.name = name
    self.color = color
fido = Dog("Fido", "brown") #instancja klasy Dog -> fido
print(fido.legs) #4
print(Dog.legs) #4
# %%
class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade
  def get_grade(self):
    return self.grade
class Course:
  def __init__(self, name, max_students):
    self.name = name
    self.max_students = max_students
    self.students = []
  def add_student(self, student):
    if len(self.students) < self.max_students:
      self.students.append(student)
      return True
    return False
  def get_average_grade(self):
    value = 0
    for student in self.students:
      value += student.get_grade()
    return value / len(self.students)
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)
course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name) #Tim
print(course.students[0].age) #19
print(course.get_average_grade()) #85.0
# %%
# class GameObject:
#     class_name = ""
#     desc = ""
#     objects = {}
#     def __init__(self, name):
#         self.name = name
#         GameObject.objects[self.class_name] = self
#     def get_desc(self):
#         return self.class_name + "\n" + self.desc
# class Goblin(GameObject):
#     def __init__(self, name):
#         self.class_name = "goblin"
#         self.health = 3
#         self._desc = "A foul creature"
#         super().__init__(name)
#     @property
#     def desc(self):
#         if self.health >= 3:
#             return self._desc
#         elif self.health == 2:
#             health_line = "It has a wound on its knee."
#         elif self.health == 1:
#             health_line = "Its left arm has been cut off!"
#         elif self.health <= 0:
#             health_line = "It is dead."
#         return self._desc + "\n" + health_line
#     @desc.setter
#     def desc(self, value):
#         self._desc = value
# goblin = Goblin("Gobbly")
# def hit(noun):
#     if noun in GameObject.objects:
#         thing = GameObject.objects[noun]
#         if type(thing) == Goblin:
#             thing.health -= 1
#             if thing.health <= 0:
#                 msg = "You killed the goblin!"
#             else:
#                 msg = "You hit the {}".format(thing.class_name)
#     else:
#         msg = "There is no {} here.".format(noun)
#     return msg
# def examine(noun):
#     if noun in GameObject.objects:
#         return GameObject.objects[noun].get_desc()
#     else:
#         return "There is no {} here.".format(noun)
# def get_input():
#     command = input(": ").split()
#     verb_word = command[0]
#     if verb_word in verb_dict:
#         verb = verb_dict[verb_word]
#     else:
#         print("Unknown verb {}".format(verb_word))
#         return
#     if len(command) >= 2:
#         noun_word = command[1]
#         print(verb(noun_word))
#     else:
#         print(verb("nothing"))
# def say(noun):
#     return 'You said "{}"'.format(noun)
# verb_dict = {
#     "say": say,
#     "examine": examine,
#     "hit": hit
# }
# while True:
#     get_input()
# %%
class A:
    def __init__(self):
        self.size = 0
    def change_size(self, new):
        self.size = new
    change_size.modifies = 'size'
print(A.change_size.modifies) #size
# %%
