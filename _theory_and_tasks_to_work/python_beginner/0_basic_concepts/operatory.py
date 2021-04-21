# %% Wyświetlanie wyniku
print('Hello world')
# %% operatory matematyczne
print(1 + 1)
print(2 - 3)
print(3 % 2)  # modulo czyli reszta z dzielenia
print(3 // 2)  # dzielenie bez reszty
print(3 / 2)
print(3 * 2)
print(3 ** 2)
# %% operatory lokalne
x = 10
x += 3
print(x)
x *= 3
print(x)
x %= 2
print(x)
# %% typy danych
# całkowite int
print(2, 3, -5, 0)
# zmienno przecinkowe float
print(1.0, -3.4, 0.5)
# ciągi tekstowe str
print('Adam', 'Ala')
# %% zmiana typów nie do wszystkich zadań
a, b, c = 4, 'ala', 3.4
print(a, b, c)
print(type(a), type(b), type(c))
# zadnaie mnożenia
print(b * a)
# aby móc wykonać zadanie +
a1 = str(a)
c1 = str(c)
print(a1, b, c1, sep=", ")
print(a1 + b + c1)
a2 = float(a)
c2 = int(c)
print(type(a2), type(c2))
print(a2, c2)

# %% podstawowe funkcje pythona do działania an typach
#print() - wyswitlanie
word = 'Hello world'
print(word)
# input() - umieszczanie danych
word2 = input('podaj cokolwiek')
print(word2)
# len() - gługość ciągu
print(len(word2))
# %% objects
object_one = []
object_two = []
object_three = object_one
object_four = object_two[:]
print(id(object_one))
print(id(object_two))
print(id(object_three))
print(id(object_four))
if (object_one == object_two):
    print("True")
else:
    print("False")
if (object_one is object_two):
    print("True")
else:
    print("False")
if (object_one is object_three):
    print("True")
else:
    print("False")
if (object_two is object_four):
    print("True")
else:
    print("False")
# %%
