# itertools - bibloteka zawierajaca przydatne funkcje
# nieskonczone iteratory
# %% count zlicza wartosc w nieskonczonosc
from itertools import count, cycle, repeat
for i in count(3):
  print(i) #3, 4, 5, 6, 7, 8, 9, 10, 11
  if i >=11:
    break
for j in cycle([1,2,3,4,5]): #iteruje w nieskonczonosc
  print(j) #1, 2, 3, 4, 5
  if j >= 5:
    break
for k in repeat(1,7): #iteruje liczbe 1 razy 7
  print(k) #1, 1, 1, 1, 1, 1, 1
# %%
from itertools import accumulate, takewhile, chain
nums = list(accumulate(range(8))) #zwraca biezaca wartosc sumy iterowanej
#0+1, 0+1+2, 0+1+2+3, 0+1+2+3+4 itd
print(nums) #[0, 1, 3, 6, 10, 15, 21, 28]
print(list(takewhile(lambda x: x<= 6, nums))) #[0, 1, 3, 6] pobiera gdy prawdziwa iterowana
nums2 = list(range(3)) #chain - łączy iteracje w jedną
print(list(chain(nums, nums2))) #[0, 1, 3, 6, 10, 15, 21, 28, 0, 1, 2]
# %%
from itertools import product, permutations
letters = ("A", "B")
print(list(product(letters, range(2)))) #[('A', 0), ('A', 1), ('B', 0), ('B', 1)]
print(list(permutations(letters))) #[('A', 'B'), ('B', 'A')]
# %%
