#range - (0,10) 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# %% range (0, n-1), (start, stop, step)
for x in range(10):
    print(x) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for y in range(0,10,2):
    print(y) #2,4,6,8
numbers = list(range(10))
print(numbers)
numbers2 = list(range(10, 0, -2))
print(numbers2) #[10, 8, 6, 4, 2]
# %%
