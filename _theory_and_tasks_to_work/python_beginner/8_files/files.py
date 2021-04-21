# %%
# w - pisz, nadpisz
# open("../teoria.txt", "w")
# r - odczyt
# open("../teoria.txt", "r")
# open("../teoria.txt")
# wb - odczyt binarny i nadpisz
# open("../teoria.txt", "wb")
# wb - odczyt binarny
# open("../teoria.txt", "rb")
# %%
file = open("../teoria.txt", "r")
print(file.read())
file.close()
# or
with open("../teoria.txt", "r") as file:
    print(file.read())
    file.close()
# %% odczyt słów a nie całości
file = open("../teoria.txt", "r")
print(file.read(6))
print(file.read(10))
file.close()
# %% readlines - z pętlą odczyt lini po linii
file = open("../teoria.txt", "r")
print(type(file.readlines()))
print(file.readlines())
for line in file.readlines():  # zwraca listę
    print(line)
file.close()
# or
file = open("../teoria.txt", "r")
for line in file:
    print(line)
file.close()

# %% write line
file = open('../teoria.txt', 'w')
file.write('dopisz tekst')
msg = "\nhello"
amount_written = file.write(msg)
print(amount_written)  # bity 6
file.close()
file = open('../teoria.txt', 'r')
print(file.read())
file.close()

# %% dodawanie tekstu
with open('../teoria.txt', 'a') as file:  # dopisywanie tekstu
    file.write('\nDodana linia')
    file.close()
with open('../teoria.txt', 'r') as file:
    print(file.read())
    file.close()

# %%
file = open('../teoria.txt', "r")
for word in file.readlines():
    word = list(word.split(' '))
    elem = [elem[0] for elem in word]
    elem = "".join(elem)
    print(elem)
file.close()
# %%
