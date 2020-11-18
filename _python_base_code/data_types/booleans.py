#True
"""Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones."""
#False
"""False, None, 0, "", (), [], {}"""
# %% Boolean logic
print(1==1) #True
print(1==1 and 2==1) #False
print(1!=1 or 2==2) #True
print(not 1 == 1) #False
# %% Boolean Operator Precedence
print(False == False or True) #True
print(False == (False or True)) #False
print((False == False) or True) #True
# %% Chaining Multiple Conditions
#Tworzenie własnego Booleana za pomocą IF
grade = 80
if (grade >= 70 and grade <= 100):
    print("Passed")
else:
    print("Not Passed")
# %% == vs is
a = [1,2,3]
b = a
print(id(a), a, id(b), b)
print(a == b) #True
print(a is b) #True
c = list(a)
print(id(c), c)
print(a == c) #True
print(a is c) #False bo inne id obiektu
# %%
