import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# zakres (2 - ilosc list,5 - ilosc wartosci)

print('2nd element on 1st dim: ', arr[0, 1])

print('5th element on 2nd dim: ', arr[1, 4])
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#Access the third element of the second array of the first array:
print(arr2[0, 1, 2])
print(arr2[1, 1, 2]) #4lista 12 element


#From the second element, slice elements from index 1 to index 4 (not included):
arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr3[1, 1:4]) # 2lista, elementy z indeksem 1-4