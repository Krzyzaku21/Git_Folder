# %%
# ? Read a file
filename = 'text.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line) # I love programing, I love programing2.
# %%
# ? Write to a file
filename = 'text.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programing.\nI love programing2.")
# %%
# ? Appending to a file
filename  = 'text.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nI love making games")
# %%
