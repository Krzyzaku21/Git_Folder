# Tuple immutable
# %%
dimensions = (200, 400, 600, 300)
# ? loop tuple
for dim in dimensions:
    print(dim) #200, 400, 600, 300
# ? overwriting tuple
dimensions = (1200, 500)
print(dimensions) #(1200, 500)
# %%
words = ("spam", "eggs", "sausages",)
print(words[0]) #spam
# %% Unpacking tuples
fruits = ("Apple", "Pear", "Banana")
f1, f2, f3 = fruits
print(f1) #Apple
print(f2) #Pear
print(f3) #Banana
# %% Tuple Unpacking 2
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a) #1
print(b) #2
print(c) #[3, 4, 5, 6, 7, 8]
print(d) #9
# %%
