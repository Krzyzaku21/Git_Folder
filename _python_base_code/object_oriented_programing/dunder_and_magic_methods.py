#magiczne metody -> __init__, __add__ etc
#tworzą funkcje które nie są normalną metodą
#przeciążanie operatorów np +, * etc... tworzą kontenery
#+, __add__(self, other), Addition;
# *, __mul__(self, other), Multiplication;
# -, __sub__(self, other), Subtraction;
# %, __mod__(self, other), Remainder;
# /, __truediv__(self, other), Division;
# <, __lt__(self, other), Less than;
# <=, __le__(self, other), Less than or equal to;
# ==, __eq__(self, other), Equal to;
# !=, __ne__(self, other), Not equal to;
# >, __gt__(self, other), Greater than;
# >=, __ge__(self, other), Greater than or equal to;
# [index], __getitem__(self, index), Index operator;
# in, __contains__(self, value), Check membership;
# len, __len__(self), The number of elements;
# str, __str__(self), The string representation
# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects (e.g., in for loops)
# __contains__ for in
# %%
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    #zwraca obiekt Vector2D(obiekt1 + obeikt2) działa jak sum
    return Vector2D(self.x + other.x, self.y + other.y)
first = Vector2D(5, 7) # x=5, y=7
second = Vector2D(3, 9) #x=3, y=9
result = first + second #dodawanie x + x or y + y
print(result.x) #8
print(result.y) #16
# %%
class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    def __sub__(self, other): #magiczna metoda odejmowania
        return self.cont - other.cont #obj1 - obj2
    def __truediv__(self, other): #dzielenie
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont]) #zapisanie odzielenia line
no1 = SpecialString(1)
no2 = SpecialString(2)
result = no1 - no2
print(result) #-1
spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)
print(spam / spam)
# spam
# ============
# Hello world!
# %%
import random
class VagueList:
  def __init__(self, cont):
    self.cont = cont
  def __getitem__(self, index):
    #list[index]
    return self.cont[index + random.randint(-1, 1)]
  def __len__(self):
    return random.randint(0, len(self.cont)*2)
vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
# %% Dunder method
class Person:
  def __init__(self, name):
    self.name = name
  def __repr__(self): #__repr__ - reprezentacja obiektu w postaci ciągu
    return f"Person({self.name})"
  def __mul__(self, x):
    if type(x) is not int:
      raise Exception("Invalid argument must be int")
    self.name = self.name * x
  def __call__(self, y):
    print("called this function", y)
  def __len__(self):
    return len(self.name)
p = Person("Tim")
print(len(p)) #3 -> __len__
p * 4
print(p) # Person(TimTimTimTim) -> __mul__
print(len(p)) #12 -> __len__
p(4) # called this function 4 ->__call__
# %%
from queue import Queue as q
import inspect

class Queue(q):
  def __repr__(self):
    return f"Queue({self._qsize()})"
  def __add__(self, item):
    self.put(item)
  def __sub__(self, item):
    self.get(item)
qu = Queue()
qu + 9
qu + 7
qu - 0
print(qu) #Queue(1)
# %%
