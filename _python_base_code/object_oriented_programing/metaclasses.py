#używane tylko w wyższej konieczności
#można sie do nich podłączyć, zmienic nimi sposób tworzenia obiektów
#wymusic pewne ograniczenia, zmienic wszystkie atrybuty
#zmianic bazę, usunąć plik, lub dziedziczyc
#tworzenie kodu bibloteki
# %%
class Test: #kalsa Test
    pass
Test = type("Test", (), {}) #klasa Test taka sama jak powyżej
# %% uzycie tej nadklasy
Test = type("Test", (), {"x" : 5})
t = Test()
t.wy = "hello"
print(t.x, t.wy) #5 hello
# %% metaclasses, subclasses, function
class Foo:
    def show(self):
        print("hi")
def add_attribute(self):
    self.z = 9
Test = type("Test", (Foo,), {"x" : 5, "add_attribute" : add_attribute})
t = Test()
t.add_attribute()
print(t.z) #9
t.show() #hi
# %%
class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a) #{'__module__': '__main__', '__qualname__': 'Dog', 'X': 5, 'Y': 8, 'HELLO':
        return type(class_name, bases, a)
class Dog(metaclass=Meta):
    x = 5
    y = 8
    def hello(self):
        print("hi")
d = Dog() #hi
print(d.X) #5
print(d.HELLO()) #None
# %%
