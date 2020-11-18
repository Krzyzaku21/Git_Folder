# map - bierze funkcje i obiekt iterowany i 
# zwraca nowy iterowany obiekt z funkcja zastosowana do kazdego elementu
# %% map(func, *iterables)
def add_five(x):
    return x + 5
nums = [1,2,3,4,5]
result = list(map(add_five, nums))
print(result) #[6, 7, 8, 9, 10]
#or using map with lambda
result2 = map(lambda x: x + 5, nums)
for item in result2:
    print(item) #6, 7, 8, 9, 10
#or using list comprehension
print([x+5 for x in nums]) #[6, 7, 8, 9, 10]
# %%
