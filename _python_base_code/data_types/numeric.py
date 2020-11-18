x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Assignment Operators
"""
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
"""
#Comparison Operators
"""
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
"""
#Logical Operators
"""
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""
# Identity Operators
"""
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y
"""
# %% Numeric Functions
print(min(1, 2, 3, 4, 0, 2, 1)) #0
print(max([1, 4, 9, 2, 5, 6, 8])) #9
print(abs(-99)) #99
print(abs(42)) #42
print(sum([1, 2, 3, 4, 5])) #15
a = 3.652
print(round(a,1)) #3.7
print(round(a,0)) #4.0
print(round(a,3)) #3.652
print(round(5.6184,2)) #5.62
# %% Ternary Operator
a = 7
status = 1 if a >= 5 else 42
print(status)
msg = "Logout" if status == 1 else "Login"
print(msg)
# %% zaokrąglenie do liczb po przecinku
import random
amount = random.uniform(1.0, 150.0)
print("%.1f" % amount)
print("%.2f" % amount)
print("%.3f" % amount)
print("%.4f" % amount)
# %%
