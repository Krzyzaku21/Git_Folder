# %% funkcja lambda
def function_lambda(a, b):
    return a + 10 + b


print(function_lambda(5, 6))  # 21
# %% lambda z wartością
x = ((lambda x: x + 2)(4))
print(x)  # 6
# %% lambda do opisywania innych funkcji


def my_fun(n):
    return lambda a: a + n


my_doubler = my_fun(2)  # wypełnia n
print(my_doubler(5))  # wypełnia a
# %%


def function(fun, arg):
    return fun(arg)


print(function(lambda x: 2*x, 5))  # 10
