#dict muttable
# %%
# ? Access value dict
alien = {
    "color" : "green",
    "points" : 5
    }
print(alien["color"]) #green
# ? Add new key-value pair
alien["spaceship_speed"] = 100
print(alien) #{'color': 'green', 'points': 5, 'spaceship_speed': 100}
# ? Looping all key-value pairs
for k, v in alien.items():
    print(k, v) #color green, points 5, spaceship_speed 100
# ? looping all keys
for k in alien.keys():
    print(k) #color, points, spaceship_speed
# ? looping all values
for v in alien.values():
    print(v) #green, 5, 100
# %%
alien = {
    "color" : "green",
    "points" : 5
    }
# ? get value dict with get()
alien_value = alien.get("color")
print(alien_value) #green
# ? change key value in dictionary
alien['color'] = "yellow"
print(alien) #{'color': 'yellow', 'points': 5}
# ? del key-value pair
del alien['points']
print(alien) #{'color': 'yellow'}
# ? ilość par key-value
print(len(alien)) #1
# %% dict **kwargs rozpakowanie słownika
def fun(a, b):
    print("1", a, "2", b) #1 value1 2 value2
keys_data = {
    "a": "value1",
    "b": "value2"
    }
fun(**keys_data)
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} is {1}".format(key, value)) #name is John
greet_me(name="John")
# %% values of dict keys
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"]) #24
print(ages["Mary"]) #42
# %% key of dict values
my_dict ={"java":100, "python":112}
key_it = [key for key, value in my_dict.items() if value == 100]
print("".join([str(x) for x in key_it])) #java
# %% dictionary Functions
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64 #dodawanie klucza i wartosci
squares[3] = 9 #zamiana wartosci dla klucza 3
print(squares) #{1: 1, 2: 4, 3: 9, 4: 16, 8: 64}
# %%
# ? Nesting dict in list
users = []
new_user = {
    'name' : 'Rob',
    'surname' : 'Dannie',
    'nickname' : 'robbie2'
}
users.append(new_user)
for user_dict in users:
    for k, v in user_dict.items():
        print(k, v) #name Rob, surname Dannie, nickname robbie2
    print("\n")
#or
users1 = [
    {
    'name' : 'Gorty',
    'surname' : 'Swart',
    'nickname' : 'swartigort'
    },
    {
    'name' : 'Edward',
    'surname' : 'Norton',
    'nickname' : 'nortik9'
    }
]
for user_dict1 in users1:
    for k1, v1 in user_dict1.items():
        print(k1, v1)
    print("\n")
# name Gorty, surname Swart, nickname swartigort
# name Edward, surname Norton, nickname nortik9
# %%
# ? Nesting list in dict
languages = {
    'Tom' : ['Python3', 'Ruby'],
    'Sally' : ['C#'],
    'Andrew' : ['GO', 'C++']
}
for name in languages.items():
    print(name, " : ") #('Tom', ['Python3', 'Ruby'])  :
    for lang in name:
        print(lang)
# Tom
# ['Python3', 'Ruby']
# ('Sally', ['C#'])  :
# Sally
# ['C#']
# ('Andrew', ['GO', 'C++'])  :
# Andrew
# ['GO', 'C++']
# %%
# ? Nesting dict in dict
users = {
    'a_einstein' : {
        'name' : 'Albert',
        'surname' : 'Einstein',
        'nickname' : 'bigbrain1'
    },
    'mcurie' : {
        'name' : 'Marie',
        'surname' : 'Curie',
        'nickname' : 'rentgen_queen'
    },
}
for username, user_dict in users.items():
    print("\nUsername: " + username) #Username: a_einstein, Username: mcurie
    full_name = user_dict["name"] + " "
    full_name += user_dict['surname']
    nick = user_dict["nickname"]
    print(f"\tFull name: {full_name.title()}") #title - zwraca tekst
    #Full name: Albert Einstein, Full name: Marie Curie
    print(f"\tNickname: {nick.title()}")
    #Nickname: Bigbrain1, Nickname: Rentgen_Queen
# %%
# ? Loop make dictionary
dict_group = {}
for x in range(5):
    dict_group[x] = x**2
print(dict_group) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# %%
# ? zip() to make dictionary
group_1 = [1, 2, 3, 4, 5]
group_2 = ["a", "b", "c", "d", "e"]

parings = {nums : alphas for nums, alphas in zip(group_1, group_2)}
print(parings) #{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# %%
# How merge two dictionaries in Python 3.9
x = {'a' : 1, 'b' : 2}
y = {'b' : 4, 'c' : 3}
z = {**x, **y}
print(z) # {'a': 1, 'b': 4, 'c': 3}
z = {**x, 'foo': 1, 'bar': 2, **y}
print(z) # {'a': 1, 'b': 4, 'foo': 1, 'bar': 2, 'c': 3}
v = y | x
print(v) #{'b': 2, 'c': 3, 'a': 1}
# %%
