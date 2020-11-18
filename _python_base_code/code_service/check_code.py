# %% inspect sprawdzanie kodu, danych itd
import random
import inspect
print(inspect.getsource(random)) #opis, kod modułu, metody,  funkcji, klasy, obiektu
# print(inspect.getfile(random)) #adres modułu, metody,  funkcji, klasy, obiektu
# print(inspect.getmodule(random)) #adres modułu, metody, funkcji, klasy, obiektu
# inspect.signature(list) #co zawiera obiekt
# inspect.getfullargspec(list)#specyfikacja obiektu czy
#iterable(policzalny), varargs-many arguments, varkw - many keys
# %% dir - wypisuje zawartosc metod kodu
print(dir(print))
# %% słowa kluczowe
import keyword
# print(keyword.kwlist) #słowa kluczowe
# print(keyword.iskeyword("or")) #sprawdzanie słowa kluczowego
# %% type -typ obiektu
type(random)
# %% help opisówka
help(random)
# %%
