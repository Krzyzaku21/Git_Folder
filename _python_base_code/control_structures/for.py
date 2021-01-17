# pętla for - liczba iteracji jest ustalona
# %% for loop in list with strings
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")  # hello!, world!, spam!, eggs!
# %% iterate strings
str = "testing for loops"
count = 0
for x in str:
    if x == "t":
        count += 1
print(count)  # 2 wystąpienia litery "t" w tekscie
# %% for with else
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")  # Unbroken 1
for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")
# %%
