# %% funkcje własne
def my_function():
    drukuj = print('my function')
    return drukuj


my_function()
# %% funkcje przyjmują ARGUMENTY
# domyślne


def printer(word):
    return print(word)


printer('witaj')
# %% przyjęte z góry


def myName(name='Johny'):
    return print(f'Imię do przyjęcia {name}')


myName()
myName('Robert')
# %% przyjmowanie argumentów list i słowników


def myPrint(a, *args, **kwargs):
    print(a)
    print("listy ", args)
    print("slownik", kwargs)


myPrint('word', 1, [1, 2, 3], 'select', {'a': 3, 'b': 2}, bry="aaa")


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} to {1}".format(key, value))


greet_me(name="Tom")
# %% wywołanie samej siebie "rekursja"
"""
1. calc(5)
2. 5 + calc(4)
3. 5 + 4 + calc(3)
4. 5 + 4 + 3 + calc(2)
5. 5 + 4 + 3 + 2 + calc(1)==1 więc 5 + 4 + 3 + 2 + 1 = 15
"""


def calc(arguments):
    if arguments == 1:
        return 1
    else:
        return arguments + calc(arguments - 1)


nums = 5
print(calc(nums))
# %% funkcja zwraca wartosc


def adds_numbers(x, y):
    return x + y


x = adds_numbers(3, 4)
print(x)

# %% programowanie funkcyjne
"""
1. multiple_function(sums, 5)
return sums(sums(5))
2.sums(x=sums(5))
return x + x=(x + x)
return x + x=(5 + 5)
return x + x=10
return 10 + 10
return 20
"""


def multiple_function(func, arg):
    return func(func(arg))


def sums(x):
    return x + x


print(multiple_function(sums, 5))

# %%


def fibb(x):
    listed = []
    for i in range(x):
        if i == 1:
            listed.append(1)
        if i == 0:
            listed.append(0)
        else:
            listed.append(listed[i] + listed[i - 1])
    return listed


fibb(10)

# %% rekursja - zwracanie samej siebie


def rec_fib(n):
    if n < 2:
        return 1
    else:
        return rec_fib(n-1) + rec_fib(n-2)


def fibb(n):
    return [rec_fib(a) for a in range(n)]


fibonacii = fibb(5)
print(fibonacii)

# %% rekurencja x jako mnoænik y jako pétla zmniejszajáca sié


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)


print(power(2, 3))  # 8
# how : (x=2,y=3) -> 2 * (x=2, y=2) -> 2 * 2 * (x=2, y=1) -> 2 * 2 * 2 * (x=2, y=0) -> 2 * 2 * 2 * 1 = 8
# %% rekurencja pośrednia - jedna funkcja wywołuje drugą a ta wywołuje pierwszą


def number_even(x):
    if x == 0:
        return True
    else:
        return number_odd(x-1)


def number_odd(x):
    return not number_even(x)


print(number_odd(5))
print(number_even(5))


# %% argumenty funkcji
def function(named_arg, *args, **kwargs):
    print(named_arg)
    print(*args, sep=',')
    print(*kwargs, *kwargs.values())


function(1, 2, 3, 4, 5, a=6, b=7)

# %% reverse rekursja


def spell(elem):
    if len(elem) == 1:
        return elem
    else:
        return spell(elem[1:]) + elem[0]


txt = 'PYTHON'

print(spell(txt))

# %%
