# %% znaki w string
print('Ala\'s have a cat\'s and \n newline is with dog\'s')
# %% formatowanie stringa zmiennymi
liczba = 352.32112
rachunek = 'Andrzej Dobierski'
f"Na fakturę pod numerem 123 wystawiono {rachunek} na kwotę {liczba}"
print(r"Dziwne znaki zapraszam   #$%^&*(#$%^&*")
multiline = """
linia pierwsza
linia druga
linia trzecia
"""
print(multiline)
cena = 50
f"cena {cena:.2f} złotych"  # .2f licba zer po przecinku
# %% funkcje string
# najwazniejsze:
# # counter, find, index, join, partition, replace, split
newString = "losowe zdanie z znakami, przecinkami. Wiele formatów"
newWord = "     Słowo"
counter = newString.count("i")  # wyliczenie występowania "i" w stringu
print(counter)
findr = newString.find('znak')  # pozycja początkowa słowa znak, jak nie znajdzie zwraca -1
print(findr)
indexr = newString.index('zdanie')  # początkowa pozycja słowa
dictionary = {'AA': 10, 'BB': 20, 'CC': 30}
joinr = newWord.join(dictionary).split()
print(joinr)
lowerr = "HELLO".lower()  # konwertuje na male litery
print(lowerr)
replacer = "Frank".replace("F", "H")  # amienia słowo/litere
print(replacer)
splitr = newString.split(',')  # dzieli okreslonym znakiem na listę
print(splitr)
# %% indeksowanie stringa
word = 'witajcie'
print(word[0])
print(word[5])
# %%
