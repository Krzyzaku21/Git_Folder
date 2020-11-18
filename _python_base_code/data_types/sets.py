#sets unikalne
# %%
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])
print(3 in num_set) #True
print("spam" not in word_set) #False
# %% Sets functions
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums) #{1, 2, 3, 4, 5, 6}
nums.add(-7)
nums.remove(3)
print(nums) #{1, 2, 4, 5, 6, -7}
# %% Sets operators
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second) #{1, 2, 3, 4, 5, 6, 7, 8, 9} dla obu wszystkie
print(first & second) #{4, 5, 6} wspolne tylko
print(first - second) #{1, 2, 3} pierwszy minus drugi
print(second - first) #{8, 9, 7} drugi minus pierwszy
print(first ^ second) #{1, 2, 3, 7, 8, 9} unikalne z pierwszego i drugiego
# %%
