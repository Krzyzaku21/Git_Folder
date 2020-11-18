## Staticmethod = funkcja niezwiązana z tą klasą.
# Używane do celów organizacyjnych (na przykład klasa Calculator
# z metodami dodawania, odejmowania, mnożenia itp.).
# Nie musisz tworzyć ani jednej instancji, aby z niej korzystać.
# %%
class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1
p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("Jill")
print(Person.number_of_people)
# %%
class Math:
    @staticmethod #dont change anything, method do something
    def add_five(x):
        return x + 5
    @staticmethod
    def add_ten(x):
        return x + 10
    @staticmethod
    def prin_t():
        print("run")
value = 3
print(value)
value1 = Math.add_five(value)
print(value1)
value2 = Math.add_ten(value)
print(value2)
Math.prin_t()

# %% Create a static method using staticmethod()
class Mathematics:
    def addNumbers(x, y):
        return x + y
# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)
print('The sum is:', Mathematics.addNumbers(5, 10))
# %% Create a utility function as a static method
class Dates:
    def __init__(self, date):
        self.date = date
    def getDate(self):
        return self.date
    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")
date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)
if(date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")
# %% inheritance works with static method
class Dates:
    def __init__(self, date):
        self.date = date
    def getDate(self):
        return self.date
    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")
class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)
date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")
if(date.getDate() == dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")
# %%
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True
    def __repr__(self):
        return "Pizza({})" . format(self.toppings)
ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
print(pizza)
# %%
class Smoothie(object):
    YOGURT = 1
    STRAWBERRY = 2
    BANANA = 4
    MANGO = 8
    @staticmethod
    def blend(*mixes):
        return sum(mixes) // len(mixes)
    @classmethod
    def eternal_sunshine(cls):
        return cls.blend(cls.YOGURT, cls.STRAWBERRY, cls.BANANA)
    @classmethod
    def mango_lassi(cls):
        return cls.blend(cls.YOGURT, cls.MANGO)
smoth = Smoothie.eternal_sunshine()
mango = Smoothie.mango_lassi()
print(smoth, "=======", mango)
class BetterSmoothie(Smoothie):
    YOGURT = 'yogurt'
    STRAWBERRY = 'strawberry'
    BANANA = 'banana'
    MANGO = 'mango'
    @staticmethod
    def blend(*mixes):
        return ', '.join(mixes)
smoth = BetterSmoothie.eternal_sunshine()
mango = BetterSmoothie.mango_lassi()
print(smoth, "=======", mango)
# %% różnica staticmethod a classmethod
class Dog:
    dogs = []
    def __init__(self, name): #prypisanie atrybutów
        self.name = name
        self.dogs.append(self) # odwołanie self do dogs
    @classmethod #funkcja mogaca dziedziczyc atrybuty innej funkcji lub klasy
    def num_dogs(cls):
        return len(cls.dogs)
    @staticmethod #funkcja odnosząca sie wyłącznie do samej siebie
    def bark(n):
        "bark n times"
        for _ in range(n):
            print("Bark!")
tim = Dog("Tim")
jim = Dog("Jim")
print(Dog.dogs) #[<__main__.Dog object at 0x059573E8>, <__main__.Dog object at 0x05957460>]
print(Dog.num_dogs()) #2 classmethod
print(tim.num_dogs()) #2 classmethod
Dog.bark(5) #Bark! * 5


# %%
