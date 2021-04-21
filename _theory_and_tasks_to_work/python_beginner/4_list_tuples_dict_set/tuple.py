# %% tuple - nie są modyfikowane, przyjmuje różne typy danych
new_tuple = ("adam", "wojtek", "roman")
print(new_tuple)
# %% tuple moze być modyfikowane przyjmując modyfikowany ciąg
new_tuple = ("adam", ['daniel'], "roman")
new_tuple[1].append('ryszard')
print(new_tuple)
# lub zmianiając typ
new_tuple = ("adam", 'franek', "roman")
lista = list(new_tuple)
lista[1] = 'wrak'
tuplek = tuple(lista)
print(tuplek)
# %% rozpakownaie tupli
new_tuple = ("adam", 'franek', "roman")
x, y, z = new_tuple
print(x)
print(y)
print(z)
# %% tuple + lub *
new_tuple = ("adam", 'franek', "roman")
dodanie = new_tuple + new_tuple
mnozenie = new_tuple * 2
print(dodanie)
print(mnozenie)
