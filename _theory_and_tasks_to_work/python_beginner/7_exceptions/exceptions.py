# %%
"""ZeroDivisionError:
Dzielenie przz zero błąd
ImportError:
błąd importu
IndexError:
Indeksowanie po za zakresem
NameError:
Nieznana zmienna
SyntaxError:
Kod nie może zostać poprawnie zrealizowany
TypeError:
Wywoływanie funkcji przez niewłaściwy typ
ValueError:
Funkcja jest wywoływana na poprawnym typie ale,
wartości w niej są nieprawidłowe
"""
# %% try except z opisaniem wyjątków - zgłaszany pierwy błąd
try:
    num = 10
    print(num + "string")
    print(num / 0)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
# %% try except finally
try:
    word = 'spam'
    print(word / 0)
except:
    print('Zgłaszanie błedów')
finally:
    print('Odpala niezależnie od wszystkiego')
# %% try except else
# else wywołuje się chyba że wystąpi błąd
try:
    print(1)  # 1
except ZeroDivisionError:
    print(2)
else:
    print(3)  # 3

try:
    print(1/0)
except ZeroDivisionError:
    print(4)  # 4
else:
    print(5)
# 1 ,3, 4
# %%
try:
    print(1)  # 1
    print(1 + '1' == 2)
    print(1)
except TypeError:
    print(3)  # 3
else:
    print(4)
# 1 3
# %% raising exception
name = '123'
raise NameError("Zła nazwa")  # NameError: Zła nazwa

# %%
