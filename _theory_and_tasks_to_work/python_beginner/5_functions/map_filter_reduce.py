# %% map (funkcja, lista)
from functools import reduce
items = [1, 2, 3]
def function(x): return x * 3


mapping = list(map(function, items))
print(mapping)
# %% filter zwraca liste elementów dla których zwraca True
numbers = [x for x in range(-5, 5)]
def function(x): return x < 0


filtering = list(filter(function, numbers))
print(filtering)
# %% reduce
items = [1, 2, 3]
def function(x, y): return x * y


reducing = reduce(function, items)  # 1 * 2 * 3 = 6
print(reducing)
