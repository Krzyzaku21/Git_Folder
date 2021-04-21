# %% operatory bool
a, b = 3, 4
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(True and False)
print(True or False)
print(not True)
my_boolean = True
print(my_boolean)
# %% kontrola przepływu
x = 50
if x > 5:
    print('highter')
elif x < 60:
    print('lower 60')
else:
    print('more')
# %%
x = 50
if x == 50:
    print('highter')
    if x < 60:
        print('lower 60')
else:
    print('more')
# %% pętla while
# pętla bez końca trzeba podać warunek by zakończyć
x = 10
while True:
    if x >= 0:
        print(f'liczba {x}')
        x -= 1
    else:
        print('end')
        break
# %%
x = 0
while x < 5:
    print(f"liczba {x}")
    x += 1
# %% while break continue
i = 1
while i <= 5:
    print(f"liczba {i}")
    i += 1
    if i == 3:
        print(f'skip {i}')
        continue
    if i == 5:
        print(f"koniec {i}")
        break

# %%
i = 0
x = 0
while i < 4:
    x += i
    i += 1
    print(i, x)
print(x)
# %% petla for
for x in range(5):
    print(x)

# %% for vs while
"""
Pętla for jest pętlą sończoną, a dla pętli while trzeba podać
Warunek przerwania pętli.
Pętla while może wykonywać to samo co pętla for tylko mniej elegancko.
"""

for i in range(5):
    print(f'pętla for liczba {i}')
    i += 1
i = 0
while i < 5:
    print(f'pętla while liczba {i}')
    i += 1
# %%


def func(x):
    res = 0
    for i in range(x):
        res += i
    return res


print(func(4))  # 0 + 1 + 2 + 3 = 6
# %%
