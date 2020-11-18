def met_pow(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return print(result)
met_pow(2, 3)

lista = [2,8,2]
a = list(range(*lista))
b = dict(x for range(lista))
print(a)


import random
# a = random.randint(1,6)
# print(a)
# b = random.randrange(1,6)
# print(b)
# c = random(1,6)
# print(c)
import keyword
# help(keyword.iskeyword)
# help(keyword)
# print(keyword.iskeyword)
# class test:
#   a = 'Foo'
#   b = 12
# o2 = type('Y', (test,), dict(a='Foo', b=12))
# import inspect
# # print(inspect.getfullargspec(z))
# print("\n")
# # print(inspect.signature(dict.keys))
# print(dir((enumerate)))
# print("\n")
# print(inspect.signature(enumerate))
# print("\n")
# print(inspect.getfullargspec(enumerate))
# print("\n")
# print(help(enumerate))
# ages = dict()
# d = {
# 'a':2, 
# "b":3
# }
# for k in d:
#     print(d[k])