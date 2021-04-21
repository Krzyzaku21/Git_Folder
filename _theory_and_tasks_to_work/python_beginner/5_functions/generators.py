# %% generatory - typ iterowany __iter__ który nie ma
# indexu który ma __next__, czyli:
# generator działa tylko 1 raz inaczej niż zapętlona pętla
def generator_function():
    for i in range(5):
        yield i


for item in generator_function():
    print(item)
# or
print(list(x for x in generator_function()))
# %%

# %%
