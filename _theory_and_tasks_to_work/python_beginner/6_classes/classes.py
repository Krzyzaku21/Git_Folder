# %% class, methods, __init__
from random import randint


class Car():
    collection = {}

    def __init__(self, model, color):
        self.collection['model'] = model
        self.collection['color'] = color

    def speed(self):
        print('wrrrr...')


car = Car('Audi', 'red')
print(car.collection)
car.speed()
# %% dziedziczenie


class Animal():
    def __init__(self, typed, continent):
        self.typed = typed
        self.continent = continent
        listed = [typed, continent]
        print(listed)


class Monkey(Animal):
    def legs(self):
        number_legs = 2
        print(number_legs)


class Dog(Monkey):
    def legs(self):
        number_legs = 4
        print(number_legs)


monkey = Monkey('Shinpanse', 'Amazonia')
monkey.legs()
dog = Dog('Rothweirrer', 'Europa')
dog.legs()


# %% funkcja super odwołująca się do funkcji nadrzędnej
class WriterOne():
    def spam(self):
        print('one')


class WriterTwo(WriterOne):
    def spam(self):
        print('two')
        super().spam()


WriterTwo().spam()


# %% magic methods - klasy niższego rzędu, wolniejsze od podstawowych
# zmiana operatorów np + dunder methodą __add__
class Sums2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Sums2D(self.x + other.x, self.y + other.y)


first = Sums2D(2, 2)
second = Sums2D(3, 5)
result = first + second  # niestandardowe zachowanie + czyli __add__
print(result.x)
print(result.y)

# %% magic methods __truediv__ to /


class SpecialString():
    def __init__(self, x):
        self.x = x

    def __truediv__(self, other):
        line = "=" * len(other.x)
        return "\n".join([self.x, line, other.x])


spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)
# spam
# ============
# Hello world!

# %%


class VagueList():
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + randint(-1, 1)]

    def __len__(self):
        return randint(0, len(self.cont)*2)


vague_list = VagueList(['A', 'B', 'C', 'D', 'E'])
print(len(vague_list))  # 9
print(len(vague_list))  # 6
print(vague_list[2])  # D
print(vague_list[2])  # D
# %% data hidding _hiddenlist


class Quene():
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def __repr__(self):
        return f"Quene({self._hiddenlist})"


queue = Quene([1, 2, 3])
print(queue)
print(queue._hiddenlist)

# %% data hidding strong private __object


class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)


s = Spam()
s.print_egg()
print(s._Spam__egg)
# %% classmethod - cls - w cls znajduje się metoda klasy z argumentami klasy
# - dekorator klasowy opisujący metodę klasy


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        print(cls.__name__)  # Rectangle klasa
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())  # 25

# %% staticmethod - instancja klasy ale bez argumentów - dekorator klasy


class Math:
    @staticmethod  # dont change anything, method do something
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
# %%


class Math:
    a = 5
    b = 5

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_nums(self):
        return self.a + self.b

    @staticmethod
    def multi_nums(a, b):
        return a * b

    @classmethod
    def multi_cls_nums(cls):
        return cls.a * cls.b


number_one = Math(3, 4).add_nums()
print(number_one)
number_two = Math.multi_nums(5, 6)
print(number_two)
number_three = Math.multi_cls_nums()
print(number_three)
# %% property - tylko do odczytu, nie moæna zmienia© atrybutów metody


class Car():
    def __init__(self, atributes):
        self.atributes = atributes

    @property
    def car_drive(self):
        return False


car = Car(['engine', 'mask', 'wheels'])
print(car.car_drive)
car.car_drive = True  # can't set attribute
# %%


class Person:
    def __init__(self, age):
        self.age = age

    @property
    def isAdulit(self):
        self.age > 18
        return True


person = Person(5).isAdulit
print(person)
# %% property dekortory setter/getter function:
# setter - ustawia wartości
# getter - poiera wartości


class Person:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return print('property')

    @age.getter
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 18:
            self._age = value
            return print(f"accept {self._age}")
        else:
            self._age = value
            return print(f"too young {self._age}")


person = Person()
person2 = Person()
print(person.age)
person.age = 7
person2.age = 30
print(person.age)
print(person2.age)

# %%

# %%
