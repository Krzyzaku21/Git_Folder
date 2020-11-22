# %% ZAD1
a = input('Wprowadz liczbe: ')
print(type(a))
b = float(input('Wprowadz liczbe: '))
b += 1
print(type(b), b)

# %% ZAD2
produkt = 12
s = 'W magazynie {} {} sztuk.'.format(produkt, produkt)
print(s)

# %% ZAD3
name = input('Podaj swoje imie: ')

if len(name) < 3:
   print('podaj minimum 3 znaki')
else:
   print(name)

# %% ZAD4
name = input('podaj nazwe jezyka programowania: ')
if name == 'python':
   print('to jest python')
elif name == 'php':
   print('To jest php')
elif name == 'java':
   print('To jest java')
else:
   print('nie znam takiego jezyka')

# %% ZAD5
a = 3
b = 4
c = 10
d = False

if a == 3 and b == 4 and c ==10:
   print('Warunek spełniony')
if a == 3 or b == 34 or c ==54:
   print('Warunek spełniony2')
if not d:
   print('Warunek spełniony3')

# %% ZAD6
a = True 
#True 1, 2, 3, 123, "jakis string"
#False 0, ' ' , None

if a == True:
   print("Warunek spełniony")

# %% ZAD7
licznik = 0
while licznik <= 10:
   licznik +=1
   print(licznik - 1)

# %% ZAD8
licznik = 1
while licznik <= 10:
   licznik +=1
   if licznik % 2 != 0:
       continue
   print(licznik)

# %% ZAD9
#typ1
while True:
   liczba = int(input('Podaj liczbe więksą od zera: '))
   if liczba > 0:
       print("Twoja liczba to:", liczba)
       break
   else:
       print("To nie jest prawidłowa liczba")

#typ2
while True:
   liczba2 = int(input('Podaj liczbę: '))
   if liczba2 > 0:
       print("To Twoja liczba: ", liczba2)
       break
   if liczba2 == 0:
       print("Twoja liczba jest po za skalą")
       break

# %% ZAD10
a = int(input('Podaj wartość a: '))
b = int(input('Podaj wartość b: '))
c = int(input('Podaj wartość c: '))
values = {a,b,c}
for v in values:
   if v % 2:
       print(v)

# %% ZAD11
for v in range(1 ,20, 3):
   print('*' * v, v)
   if v % 2 !=0:
       print('*' * v, v)

# %% ZAD12
my_list = [1,2,3.5, 's', True]
my_list[4] = 20
print(my_list)

# %% ZAD13
my_list = [10, 20, 30, 40]
my_list.append(5) #dokleja wartość na końcu listy na obiekcie
my_list.append(3)
my_list.append(45)
my_list.append(77)
my_list.sort() #sortuje liczby
my_list.reverse() #odwraca wartości listy
print(my_list)

for v in my_list:
   print(v)

# %% ZAD14
my_list = [10, 20, 30, 40]
my_list_2 = [50, 60]
main_list = my_list + my_list_2
print(10 in main_list)

# %% ZAD15
my_list = [v for v in range(9, 27) if v % 2 == 0 ] #wartosci spełniajace wartosci parzyste tylko wypisze
print(my_list)

# %% ZAD16
#tuple
values = (1,2,3, 'abc', True) #nie mozna modyfikowac wartosci tuple, ani zmieniac ani dopisywac itp
for v in values:
    print(values[2])

# %% ZAD17
values = (1, 2, 3, 4, 5, 6, 7)
new_values = values[:3]
print(len(new_values + (10, 20, 30)))

# %% ZAD18
# tuples prydatne operacje
my_list = [10 , 4, 5, 17, 7, 2, 5]
my_tuple = tuple(my_list)
#print(sum(my_tuple)) #len - długość elementów, max - największa wartość z listy, min - najmniejsza wartosc z listy, sum - suma wartosci
a, b, c, d, e, f, g = my_tuple
print(a)

# %% ZAD19
options = {
   'env' : 'production',
   'db' : 'mysql',
   'version' : 1.0,
   'show_errors' : True
}
options['user'] = 'admin'
options['version'] = 2.0
print(options['env'], options['version'], options['user'])

# %% ZAD20
options = {
   'env' : 'production',
   'db' : 'mysql',
   'version' : 1.0,
   'show_errors' : True
}

del options['db'] #del - usówanie klucza z obiektu
options.update({
   'user' : 'admin',
   'app' : 0,
   'version' : 2.2
   })
#print(options.values()) #values - zwraca wszystkie wartosci listy
print(options.keys()) #keys - metoda zwracajaca wszystkie klucze
for key in options:
   print(options[key])
print(options.get('version')) #get wyciaganie klucza

# %% ZAD21
a = set([1, 2, 3, 4]) #set - funkcja zbiór unikalnych wartości
b = set([1, 3, 7 ,9])
#print(a.intersection(b)) #intersection - czesc wspolna zbioru a i b
#print(a.union(b)) #union - połączenie bioru a i b
print(a.difference(b)) #difference - elementy unikalne dla zbioru a inne od zbioru b
print(a.symmetric_difference(b)) #symmetric_difference - elementy unikalne dla zbioru a i b

# %% ZAD22
#Tworzenie własnej unikalnej funkcji
def fn():
   print('Witaj')
fn()

# %% ZAD23
def fn(a, b):
   print(a + b)
fn(3, 4)

# %% ZAD24
def fn(a, b=0, c=0):
   print('a:', a, 'b:' , b, 'c:', c)
fn(2, c=5)

# %% ZAD25
def fn(a, *args, **dict_args): #*args - dane typu turple (obiektu co zbiera wszystkie argumenty)
   print(a) #**dict_args - wsystkie dane z args beda dodane do dictionery
   print(args[0])
   print(args)
   print(dict_args)
   for arg in args:
       print(arg)
   for key in dict_args:
       print(dict_args[key])
fn(3, 2, 4, 5, True, 'cx', user='admin', version=1.0)

# %% ZAD26
def fn(a,b):
   return a + b, a * b, a - b
r =fn(3,4)
print(r[0])

# %% ZAD27
#funkcja anonimowa lambda
double = lambda a: a * 2
square = lambda a: a * a
print(type(double))
print(square(3))

# %% ZAD28
#Scope
x = 1 #ma zasięg globalny w całym kodzie
def fn():
   global x
   x += 1
   y = 3
   print(x, y)
fn()
print(x)

# %% ZAD29
class Point:
   pass #place holder pusta klasa
p1 = Point()
print(type(p1))

# %% ZAD30
class Point:
   def __init__(self, x, y):
       self.x = x
       self.y = y
p1 = Point(3, 5)
p2 = Point(2, 7)
print(p1.x, p1.y)
print(p2.x, p2.y)

# %% ZAD31
class Point:
   def __init__(self, x=0, y=0):
       self.x = x
       self.y = y
   def move__to_new_coords(self, x=0, y=0):
       self.x = x
       self.y = y
p1 = Point(3, 5)
print(p1.x, p1.y)
p1.move__to_new_coords(12, 4)
print(p1.x, p1.y)

# %% ZAD32
#Atrybuty klasy odwołujące się do klasy
class Point:
   points_counter = 0
   def __init__(self, x=0, y=0):
       self.x = x
       self.y = y
       Point.points_counter += 1
   #def move__to_new_coords(self, x=0, y=0):
   #    self.x = x
   #    self.y = y
p1 = Point(3, 5)
print(Point.points_counter)
p2 = Point(4, 9)
print(Point.points_counter)
print(p1.points_counter)

# %% ZAD33
#dziedziczenie miedzy klasami
class Widget:
   def __init__(self, label):
       self.label = label

class Button(Widget):
   def __init__(self, label, size):
       super().__init__(label) #super - odwołuje do init w klasie Wiget
       self.size = size
   def handle_click(self):
       return 'Klik'
b = Button('my button', 'large')
print(b.label, b.size)
print(b.handle_click())

# %% ZAD34
#obiekt ma swoje atrybuty kazdy inne
a = 10
b = 'abc'
print(dir(a)) #dir - atrybuty obiektu a
print(dir(b)) #dir - atrybuty obiektu
print(b.capitalize()) #capitalize - wypis stringu z wielkiej litery an początku
def fn():
   return
print(dir(fn))

# %% ZAD35
#Mutowalność
a = [1, 2] #lista mutowalna
a[0] = 10000
print(a[0])
my_list = [3, 4]
my_tuple = (1, 2, my_list) #my_list jest typem listy która jest mutowalna w niemutowalnym tuple
print(my_tuple)
my_tuple[2].append(5)
print(my_tuple)

# %% ZAD36
#identyczność oraz równość
a = [1, 2, 3]
b = [1, 2, 3]
c = list(a)
print(a == b, a is b, id(a), id(b))
print(a is not b)
print(a is c)

# %% ZAD37
def add(a, b):
   return a + b
def multiply(a, b):
   return a * b
def apply(fn, a, b):
   return fn(a, b)
r1 = apply(add, 4, 5)
r2 = apply(multiply, 4, 8)
print(r1, r2)

# %% ZAD38
#Dekoratory
def my_decorator(fn):
   def wrapper():
       print("Początek odliczania")
       fn()
       print("Koniec odliczania")
   return wrapper

@my_decorator
def get_5_values():
   for v in range(1,6):
       print(v)

# get_5_values()
# get_5_values_decorated = my_decorator(get_5_values)
# get_5_values_decorated()
get_5_values()

# %% ZAD39
#Generator typu int
def number_generator(end):
   n = 1
   #nums = []
   while n < end:
    #    nums.append(n)
       yield n #yield - forma zwracania, iteracja
       n += 1
       #return nums
values = number_generator(100)
#print(values)
#print(next(values)) #next - funkcja zwraca kolejną wartość z interatora
#print("coś innego")
#print(next(values))
for v in values:
   print(v)

# %% ZAD40
#moduły implementacja z modułu
import sys #moduł sys - moduł platformy, wersji itp
print(dir(sys))
print(sys.version, sys.platform)
import random
print(dir(random))
print(random.randint(1,5)) #randint - zwracanie losowego zakresu liczb int z 1 - 5

from random import randint
from sys import version
print(version, randint(1,5))

# %% ZAD41
#definiowanie własnego modułu
#import my_module
# from my_module import *
# from my_module import my_function
# msg = my_module.my_function('Radek')
# msg = my_function('Radek')
# print(msg)
# print(x)
#print(my_module.x)

# %% ZAD42
#błędy i wyjątki
try: # spróbuj wykonać
   print('Próbujemy podzielić')
   a = 2 / 'abc'
   print(a)
except TypeError: # spróbuj wykonać z wyjątkiem except
   print('Błąd - niewłasciwy typ dzielnika')
try:
   b = 2 / 0
   print(b)
except ZeroDivisionError:
   print('Bład dzielenie przez zero')

# %% ZAD43
#instrukcja raise
def divide(a, b):
   if b == 0:
       #raise RuntimeError('Błąd')
       raise ZeroDivisionError('Błąd')
   return a // b
try:
   r = divide(4, 0)
   print(r)
#except RuntimeError:
except ZeroDivisionError:
   print('nie można podzielić przez zero')

