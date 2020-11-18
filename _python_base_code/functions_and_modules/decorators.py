# decorator - stosowane gdy nie chces modyfikować istniejacych
# funkcji a chcesz rozszerzyć ich funkcjonalność
# %%
def decorator(func):
    def wrap():
        print("=========")
        func()
        print("=========")
    return wrap
def print_text():
    print("Hello world")
decorated = decorator(print_text)
decorated()
# %%
def decorator(func):
    def wrap():
        print("=========")
        func()
        print("=========")
    return wrap
#dekorowanie @
@decorator
def print_text():
  print("Hello world!")
print_text()
# %%
