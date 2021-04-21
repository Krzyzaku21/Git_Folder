# %% dictionary - słownik jest: klucz : wartosc
# %%
# nieuporządkowany np:
new_dict = {
    "name": "Piotr",
    "surname": "Walczak",
}
new_dict2 = {
    "surname": "Walczak",
    "name": "Piotr",
}
print(new_dict == new_dict2)  # True
# %% odwólanie wyłącznie po istniejących kluczach
new_dict = {
    "name": "Piotr",
    "surname": "Walczak",
    "wiek": 32,
    "wzrost": 192
}
print(new_dict['surname'])  # Walczak
# %% słownik jest modyfikowalny:
new_dict = {"name": "Piotr"}
new_dict['name'] = 'Tomek'
print(new_dict)
# %% słownik dodawanie kluczy
new_dict = {"name": "Piotr"}
new_dict['second name'] = 'Tomek'
print(new_dict)
# %% dictionary Methods
# popularne keys, values, update, get, items, fromkeys
new_dict = {
    "name": "Piotr",
    "surname": "Walczak",
    "wiek": 32,
    "wzrost": 192
}
new_dict2 = new_dict.copy()
print(new_dict2)  # kopia dict
print(new_dict2.get('name'))  # Piotr
print(new_dict2.keys())  # klucze
print(new_dict2.values())  # wartosci
print(new_dict2.items())  # klucze i wartosci
new_dict2.update({'name': 'Karol', 'second name': 'Daniel'})  # update
print(new_dict2)
new_dict2 = {
    "name": "Piotr",
    "surname": "Walczak",
    "wiek": 32,
    "wzrost": 192
}
new_dict2.pop('wiek')  # usuwa specyficzną komórkę lub ostatnią
print(new_dict)
lista = ['hello', 'jack', ' sparrow']
fromkeys_dict = dict.fromkeys(lista, 'all values')
print(fromkeys_dict)
# %% pętla dla dict:
new_dict = {
    "name": "Piotr",
    "surname": "Walczak",
    "wiek": 32,
    "wzrost": 192
}
for x in new_dict.values():
    print(x)

# %% tuples as keys because not immutable
tuple_key_dict = {
    (1, 2, 3): 'one two three'
}
print(tuple_key_dict)
