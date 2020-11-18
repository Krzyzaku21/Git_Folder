#assert - sprawdzanie napisanego programu (testowanie)
# %% assert add test
x, y = 2, -3
def assert_test(x, y):
    goal = x + y
    assert(goal >= 0), "Under minus value Error" #nieprawda zgłasza bład
print(assert_test(x, y))
# %%
#raise - zgłoszenie wyjątku
x = -1
if x < 0:
    raise Exception("Sorry no number below zero")
# %%
