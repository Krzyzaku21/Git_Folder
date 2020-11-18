#instalacja - pip install library_name
# popularne moduły
# re, datetime, math, random, os, multiprocessing, subprocess,
# socket, email, json, doctest, unittest, pdb, argparse, sys
# %% modules - random
import random
for i in range(5):
   value = random.randint(1, 6)
   print(value) #losowe 5 liczb z zakresu 1-6
# %% modules math
import math
num = 10
num2 = 2
print (math.pow(num, num2)) # 10^2 -> 100
# %% modules from import
from math import pi, sqrt
print(pi) #3.141592653589793
# %% modules import as
from math import sqrt as square_root
print(square_root(100)) #10.0
# %%
import mymodule
mymodule.greeting("Jonathan")
a = mymodule.person1["age"]
print(a)
# %%
