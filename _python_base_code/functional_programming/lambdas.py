#lambda - pojedyncza linia kodu
# %%
def my_function(func, arg):
    return func(arg)
my_function(lambda x: 2 * x * x, 5) #50
# %%
score = (lambda x, y, z: x * y * z)(x=1, y=2, z=3)
print(score) #6
# %%
double = lambda x, y, z: x * y + z
print(double(7, 2, 1)) #15
# %%
