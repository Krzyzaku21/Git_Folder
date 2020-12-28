
from itertools import product, permutations


def fn(box):
    if type(box) is dict:
        foo = box.items()
        for z in (box):
            if type(box[z]) is str or int or float:
                print(type(z), "key:", z, "value:", box[z], "\t")
            if type(box[z]) is list or dict or set or tuple:
                values = [l for (k, l) in foo]
                for g in values:
                    print(g)
                    if len(str(g)) > 1:
                        print(g)
                # print(values)
                # print(values_more)
                # if values_more > 1:
                #         print((l))
                #         break
    else:
        for i, x in enumerate(box):
            print(type(x), x, "\t", "index:", i)
            while type(x) is list:
                for j, y in enumerate(x):
                    print(type(y), y, "index:", j)
                break
    print("")


liczby = range(0, 5)
tekst = "tekst"
tuple_num = 1, 2, 3, 4, 5
tuple_str = "a", "b", "c", "d", "e"
list_1 = [1, "a", [1, 2, True], True]
set_1 = {1, "a", 2}
dict_1 = {
    "a": 1,
    "b": 2,
    "c": (1, 2, 3, 4, 5)
}
fn(liczby)
fn(tekst)
fn(tuple_num)
fn(tuple_str)
fn(list_1)
fn(set_1)
fn(dict_1)

a = [x*10 for x in range(5, 9)]


def pure_function(x, y):
    temp = x + 2*y
    print(temp)
    return temp / (2*x + y)


print(pure_function(1, 2))


def add_five(x):
    return x + 5


nums = [11, 22, 33, 44]
result = list(map(add_five, nums))
print(result)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


print(factorial(5))

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))


class Human:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def present(self):
        print("{0}: {1} cm".format(self.name, self.size))


class Worker(Human):
    def __init__(self, name, size, job):
        super().__init__(name, size)
        self.job = job

    def present(self):
        super().present()
        print(self.job)


w = Worker("Bob", 185, "trader")
w.present()


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)


class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)
queue.push(10)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)


class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("Hi")

    #  @classmethod
   # def sayHi(cls):
     #   print ("Hi")


Person.sayHi("Pankaj")
