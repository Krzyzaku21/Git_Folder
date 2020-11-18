# %% *args - wiele argumentów
def function(named_arg, *args):
    print(named_arg) #1
    print(args) #(2, 3, 4, 5)
function(1, 2, 3, 4, 5)
# %% food="spam" - domyślne wartości
def function(x, y, food="spam"):
    print(food)
function(1, 2) #spam
function(3, 4, "egg") #egg
# %% **kwargs - argumenty klucz - wartosc dict
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)
my_func(2, 3, 4, 5, 6, a=7, b=8) #{'a': 7, 'b': 8}
# %%
