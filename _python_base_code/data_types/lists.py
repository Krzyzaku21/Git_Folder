# %% OPERACJE NA LISTACH
# ? Loop list:
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print(i) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# ? Add item:
numbers.append(12)
print(numbers)
# ? Making numerical list:
squares = []
for x in range(1, 11):
    squares.append(x**2)
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# ? List comprehensions
score = [x * 2 for x in range(1, 6)]
print(score) #[2, 4, 6, 8, 10]
# ? Slices list
even = numbers[:3]
print(even) #[1, 2, 3]
# ? Copy list
numbers2 = numbers[:]
print(numbers2) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
print(id(numbers), id(numbers2)) # 106361320 106362600
# %% OPERACJE NA LISTACH 2
users = ['val', 'tom', 'bob', 'mia', 'ron', 'ned']
# ? get select element from list
second_user = users[1]
print(second_user) #tom
# ? channing element in list
users[2] = 'ronald'
print(users) #['val', 'tom', 'ronald', 'mia', 'ron', 'ned']
# ? add elem to end list
users.append('fiona')
print(users) #['val', 'tom', 'ronald', 'mia', 'ron', 'ned', 'fiona']
# ? insert at particular position list
users.insert(0, 'adam')
print(users) # ['adam', 'val', 'tom', 'ronald', 'mia', 'ron', 'ned', 'fiona']
# ? delete element in list
del users[0] #['val', 'tom', 'ronald', 'mia', 'ron', 'ned', 'fiona']
print(users)
users.remove('val')
print(users) # ['tom', 'ronald', 'mia', 'ron', 'ned', 'fiona']
# ? pop last item from list and first item
users.pop()
print(users) #['tom', 'ronald', 'mia', 'ron', 'ned']
users.pop(0)
print(users) #['ronald', 'mia', 'ron', 'ned']
# ? lenght of list
print(len(users)) #4
# ? sort permanently
users.sort()
print(users) #['mia', 'ned', 'ron', 'ronald']
# ? sort permanently in reverse alphabetical
users.sort(reverse=True)
print(users) #['ronald', 'ron', 'ned', 'mia']
# ? sorting a list temporarily
print(sorted(users)) #['mia', 'ned', 'ron', 'ronald']
print(sorted(users, reverse=True)) #['ronald', 'ron', 'ned', 'mia']
# ? reversing the order of a list (odwrotna lista)
users.reverse()
print(users) #['mia', 'ned', 'ron', 'ronald']
# ? print items from list
for user in users:
    print(user) #mia, ned, ron, ronald
# %%
ages = [89, 21, 45, 87, 22, 11, 3, 85, 67, 56]
# ? find max in list
print(max(ages)) #89
# ? find min in list
print(min(ages)) #3
# ? sum list ages
print(sum(ages)) #486
# %%
# ? loop vs comprehensions in list
names = ['bob', "troy", 'gabriel']
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names) #['BOB', 'TROY', 'GABRIEL']
#or using comprehensions
upper_names = [name.upper() for name in names]
print(upper_names) #['BOB', 'TROY', 'GABRIEL']
# %%
# ? removing from list
pets = ['dog', 'cat', 'fish', 'rabbit', 'pig']
print(pets) #['dog', 'cat', 'fish', 'rabbit', 'pig']
while 'cat' in pets:
    pets.remove('cat')
print(pets) #['dog', 'fish', 'rabbit', 'pig']
#%% items of list
words = ["Hello", "world", "!"]
print(words[0]) #Hello or print(words[-3])
print(words[1]) #world or print(words[-2])
print(words[2]) #! or print(words[-1])
# %% items of list in list
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1]) #0
print(things[2]) #[1,2,3]
print(things[2][2]) #3
# %% pusta lista
empty_list = []
print(empty_list)
# %% 2D grids
m = [
    [1, 2, 3],
    [4, 5, 6]
    ]
print(m[1][2]) #6
print(m)
import numpy as np
nn = np.array([[1,2,3],[4,5,6]])
print(nn)
# %% rotate list by n
n = 2
list_1 = [1,2,3,4,5]
rotate_list = (list_1[-n:] + list_1[:-n])
print(rotate_list) #[4, 5, 1, 2, 3]
# %% del elements from list
list_1 = [1,2,3,4,5]
del list_1[:]
print(list_1) #[]
# %% List comprehensions
cubes = [i**3 for i in range(5) if i**3 < 20]
print(cubes) #[0, 1, 8]
# to samo co:
list_1 =[]
for i in range(5):
    if i**3 < 20:
        list_1.append(i**3)
print(list_1) #[0, 1, 8]
# %% operator * list
list_1 =[2,7,2]
list_2 = list(range(*list_1))
print(list_2) #[2,4,6]
# %% *argv - losowe domyślne argumenty
def fun(*argv):
    print(", ".join(map(str, argv)))
fun(1,2,"a")
# %% sort() or sorted() list
#sort() - modyfikuje orginalną liste, sorted() - zwraca nową liste
list_1 = [2,4,6,3,1,5]
print(id(list_1)) #261654248
list_1.sort()
print(id(list_1),list_1) #261654312 [1, 2, 3, 4, 5, 6]
list_2 = [2,4,6,3,1,5]
print(id(list_2),list_2) #81587880 [2, 4, 6, 3, 1, 5]
list_2 = sorted(list_2)
print(id(list_2),list_2) #261661064 [1, 2, 3, 4, 5, 6]
# %% List Functions
nums = [1, 2, 3]
nums.append(4) #dodaje do końca listy
print(nums) #[1, 2, 3, 4]
print(len(nums)) #4 - długość listy
index = 1 #pozycja umieszczenia
nums.insert(index, 4)
print(nums) #[1, 6, 2, 3, 4]
print(nums.count(4)) #liczba wystąpień liczby 4 w liście nums
# %% List Slices
slices_list = [0,1,2,3,4,5,6,7,8,9,10]
print(slices_list[0:5]) #[0, 1, 2, 3, 4]
print(slices_list[:9]) #[0, 1, 2, 3, 4, 5, 6, 7, 8]
print(slices_list[9:]) #[9, 10]
print(slices_list[::2]) #[0, 2, 4, 6, 8, 10]
print(slices_list[9:-1]) #[9]
# %%
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
   print("All larger than 5") #wszystkie prawdziwe
if any([i % 2 == 0 for i in nums]):
   print("At least one is even") #jeden prawdziwy
for v in enumerate(nums): #indeksowanie
   print(v) #(0, 55)(1, 44)(2, 33)(3, 22)(4, 11)
for s in enumerate(nums, -1):
    print(s) #(-1, 55)(0, 44)(1, 33)(2, 22)(3, 11)
# %%
