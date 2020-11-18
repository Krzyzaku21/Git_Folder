# %%
# ? JSON write file
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
# %%
# ? JSON read file
import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers) #[2, 3, 5, 7, 11, 13]
# %%
# ? JSON data exists

import json

f_name = 'numbers.json'

try:
    with open(f_name) as f:
        numbers = json.load(f)
except FileNotFoundError:
    msg = f'Cant find file: {f_name}'
    print(msg)
else:
    print(numbers) #[2, 3, 5, 7, 11, 13]
# %%
