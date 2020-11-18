# ImportError: an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly;
# TypeError: a function is called on a value of an inappropriate type;
# ValueError: a function is called on a value of the correct type, but with an inappropriate value.
# %%
try:
   print(1)
   print(10 / 0)
except ZeroDivisionError:
   print("unknown_var")
finally:
   print("This is executed last")
# %%
# ? catching an exception
prompt = "How many tickets do you need?"
num_tickets = input(prompt)

try:
    num_tickets = int(num_tickets) #input int value
except  ValueError:
    print("Try again") #input no int value
else:
    print("Ticket printed")
# %%
f_names = ['alice.txt', 'bob.txt', 'text.txt']
print(f_names)
for f_name in f_names:
    try:
        with open(f_name) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("file dont exists")
    else:
        num_lines = len(lines)
        msg = f'{f_name} has {num_lines}'
        msg += ' lines.'
        print(msg)
#file dont exists
#file dont exists
#text.txt has 3 lines.
# %%
print('q to quick') #q to quick
while True:
    x = input('First number: ')
    if x == 'q':
        break
    y = input('Second number')
    if y == 'q':
        break

    try:
        result = int(x) / int(y)
    except ZeroDivisionError:
        print('cant divide by Zero') #cant divide by Zero
    except ValueError:
        print('Its must be int value') #Its must be int value
    else:
        print('%.2f' % result) # 3/4 = 0.75
# %%
