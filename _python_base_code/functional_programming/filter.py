# Filtr funkcji filtruje element iterowalny, usuwając elementy,
# które nie są zgodne z predykatem (funkcja zwracająca wartość logiczną)
# %%
nums = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x: x -5 > 0, nums))
print(result) #[6, 7, 8, 9, 10]
# %%
def bdb(item):
    result = [x - 5 for x in item if (x - 5) < 5]
    return result
nums = [1,2,3,4,5,6,7,8,9,10]
result2 = filter(bdb(nums), nums )
bdb(nums) #[-4, -3, -2, -1, 0, 1, 2, 3, 4]
# %%
