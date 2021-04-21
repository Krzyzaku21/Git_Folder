# %% dekoratory - do rozszerzania modyfikacji funkcji
def decorator(func):
    def wrapper():
        x = func()
        return x * x
    return wrapper


@decorator
def sums():
    return 10


print(sums())  # 100
# %%


def decor(func):
    def wrapper():
        print("Przed funkcją")
        func()
        print('Po funkcji')
    return wrapper


def print_text():
    print('hello world')


decorated = decor(print_text)
decorated()
# lub


@decor
def print_text2():
    print('hello world2')


print_text2()
# %%
