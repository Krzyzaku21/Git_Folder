# Funkcje
# %%
# ? simple function
def greet_user():
    print("Hello!")
# ? Passing argument


def greet_user2(username):
    print("Hello", username)


greet_user2("John")  # Hello John
# ? Default values for parameters


def make_pizza(toppings="bacon"):
    print("Topping pizza ", toppings)


make_pizza()  # Topping pizza  bacon
make_pizza("pepperoni")  # Topping pizza  pepperoni
# ? Returning value


def add_numbers(x, y):
    return x + y


sums = add_numbers(3, 5)
print(sums)  # 8
# %%
# ? Returning dictionary


def build_person(first, last):
    person = {
        'first': first,
        'last': last
    }
    return person


musician = build_person('Jimi', 'Hendrix')
print(musician)  # {'first': 'Jimi', 'last': 'Hendrix'}
# %%
# ? Function dictionary with add values


def build_person(first, last, age=None):
    person = {
        'first': first,
        'last': last
    }
    if age:
        person['age'] = age
    return person


musician = build_person('Jimi', 'Hendrix', 27)
print(musician)  # {'first': 'Jimi', 'last': 'Hendrix', 'age': 27}
musician = build_person("Jannis", "Brown")
print(musician)  # {'first': 'Jannis', 'last': 'Brown'}
# %%
# ? Passing list like argument


def greet_users(names):
    for name in names:
        msg = f"Hello, {name}"
        print(msg)


usernames = ['Hannah', 'Rick', 'Maddy']
greet_users(usernames)  # Hello, Hannah, Hello, Rick, Hello, Maddy
# %%
# ? allow list functions to a function


def print_models(unprinted, printed):
    while unprinted:
        current_model = unprinted.pop()
        print(f"Prinnting {current_model}")
        printed.append(current_model)


orginal = ['phone case', 'pendant', 'ring']
unprinted = []
printed = []
print_models(orginal[:], printed)
print(f'\nOrginal: {orginal}')  # Orginal: ['phone case', 'pendant', 'ring']
print(f'\nUnprinted: {unprinted}')  # []
print(f'\nPrinted: {printed}')  # Printed: ['ring', 'pendant', 'phone case']
# %%
# ? collect abilitary number of arguments


def make_pizza(size, *toppings):
    """Make Pizza"""
    print(f"\nMaking a {size}, pizza.")  # Making a small, pizza.
    print("Toppings:")  # Toppings:
    for topping in toppings:
        print(f" - {topping}")  # - pepperoni


make_pizza('small', 'pepperoni')
make_pizza('large', 'bacon bits', 'pineapple')
make_pizza('medium', 'mushrooms', 'peppers', 'onions', 'cheese')
# %%
# ? collect abilitary number of keyword arguments


def build_profile(first, last, **user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info


user_0 = build_profile('Marie', 'Curie', location='paris', field='chemistry')
user_1 = build_profile('Albert', 'Einstein', location='princeton')

print(user_0)  # {'location': 'princeton', 'first': 'Albert', 'last': 'Einstein'}
print(user_1)  # {'location': 'paris', 'field': 'chemistry', 'first': 'Marie', 'last': 'Curie'}
# %% Function with no arguments


def my_function():
    print("spam")


my_function()  # spam
# %% Function with arguments


def my_function_arg(word):
    print(word + "!")


my_function_arg("spam")  # spam!


def fun_add_arg(x, y):
    print(x + y)


fun_add_arg(5, 3)  # 8
# Function arguments applies only inside function


def function(argument):
    argument += 10
    print(argument)


function(7)  # 17
# print(argument) <- NameError - nie można sie odnieść
# %% Function returning


def fun_max(x, y):
    if x > y:
        return x
    else:
        return y


z = fun_max(7, 3)
print(z)  # 7


def add_nums(x, y):
    total = x + y
    return total


print(add_nums(4, 5))  # 9
# %% Functions as object


def multiply(x, y):
    return x * y


a = 4
b = 7
operaction = multiply  # funkcja jako obiekt
print(operaction(3, 2))  # 6
# %% Function used as argument


def adding(x, y):
    return x + y


def twice(func, x, y):
    return func(func(x, y), func(x, y))  # adding(adding(5,10), adding(5,10)) -> adding(15, 15) -> 30


a = 5
b = 10
print(twice(adding, a, b))  # 30
# %% Function hight-order(wyższego rzedu) niż inne


def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


# apply_twice return -> add_five(add_five(10)) ->
# -> add_five(10+5) -> add_five(15) -> add_five(15+5) -> 20
print(apply_twice(add_five, 10))  # 20
# %% Pure Functions - czysta funkcja


def pure_function(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)


print(pure_function(2, 3))  # 1.1428571428571428
# Inpure function
some_list = []


def inpure_function(arg):
    some_list.append(arg)


inpure_function(11)
print(some_list)
# %% Recusion Function - odniesienie do samej siebie
# (stosuje sie w przypadku podproblemow tego samego typu problemu co główny)


def factorial(x):
    if x == 1:
        return 1  # zabezpieczenie przed memory crash
    else:
        return x * factorial(x-1)


# 3! -> x=3 -> factorial(3) * factorial(3-1) * factorial(2-1) ->
# 3 * 2 * 1 -> 6
print(factorial(3))  # 6
# %% Recursion Functions - jedna odnosi sie do drugiej


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)  # False


def is_odd(x):
    return not is_even(x)  # zaprzeczenie even


print(is_odd(5))  # True
print(is_even(15))  # False
# %%
