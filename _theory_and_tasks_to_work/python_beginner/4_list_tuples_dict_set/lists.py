# %%
words = ['hello', 'jack', 'sparrow']
print("słowa z listy:", *words)
# %% indeksowanie w liście
words = ['hello', 'jack', 'sparrow']
print(words[0])
print(words[1])
print(words[2])
print(words[-1])

# %% listy macierze 2D lub 3D i ich indeksy
macierz = [
    [1, 2, 3], [4, 5, 6]
]
print(macierz[0][0])
print(macierz[0][2])
print(macierz[1][1])
print(macierz[1][2])
# %% operacje na listach
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)
print([i * 3 for i in nums])

# %% list slices
words = ['hello', 'jack', 'sparrow', 'have', 'a', 'black', 'pearl']
print(words[0:3])
print(words[3:])
print(words[:3])
print(words[2:6])
print(words[::-1])

# %% list metody
# append, extend, pop, sort, index, remove, insert, count, reverse
# copy, clear
words = ['hello', 'jack', 'sparrow', 'have', 'a', 'black', 'pearl']
append_list = words[:]
append_list.append('now')  # dodaje na koncu
print(append_list)
clear_list = words[:]
clear_list.clear()  # czysci liste
print(clear_list)
copy_list = words[:]
copy_list.copy()
print(copy_list)
count_list = words[:]
count_list = count_list.count('jack')  # zwraca ilosc poprawnych wyszukan
print(count_list)
extend_list = words[:]
extend_list.extend(['drown'])  # dodaje policzalne ciągi np str, listy tuple, set, dict itd.
print(extend_list)
index_list = words[:]
index_list = index_list.index('sparrow')  # zwraca pozycje elementu w liscie
print(index_list)
insert_list = words[:]
insert_list.insert(0, 'drown')  # dodaje na podanej lokalizacji
print(insert_list)
pop_list = words[:]
pop_list.pop(2)  # usuwa z okreslonej pozycji
print(pop_list)
remove_list = words[:]
remove_list.remove('jack')  # usuwa okreslony eement z listy
print(remove_list)
reverse_list = words[:]
reverse_list.reverse()  # odwraca kolejnosc listy
print(reverse_list)
sort_list
sort_list = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]


def myFunc(e):
    return e['year']


sort_list.sort(key=myFunc)  # sortuje
print(sort_list)
# %% list comprehensions -zasięg
numbers = [x for x in range(5)]
print(numbers)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]  # wypisuje liste z wyjatkiem wartosci "apple"
print(newlist)
# %% change items in list
numbers = [x for x in range(5)]
numbers[2] = 'wpis'  # zmiana 2 w liscie na 'wpis'
print(numbers)

# %%
