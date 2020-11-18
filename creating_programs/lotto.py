#symulator liczb lotto
# %%
from random import  randint as ran
set_nums = set()
def big_lotto():
    while len(set_nums) != 6:
        random_nums = int(ran(1,49))
        set_nums.add(random_nums)
    str_nums = "".join(str(set_nums).replace("{", "")).replace("}", "")
    print(f" Win numbers are: {str_nums}")
big_lotto()
# %%
