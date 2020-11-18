# %%
import pandas
df = pandas.read_csv('_python_learning\File Handling in Python\hrdata.csv')
print(df)
# %%
import csv, os
with open('C:\\Users\\Krzyz\\Desktop\\Radek Python\\_python_learning\\File Handling in Python\\names.csv', mode='r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for line in csv_reader:
        print(line)
print(csv_reader)
# %%
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
with open('file_op.txt', mode='r') as txtfile:
    fstr = txtfile.read()
    print(fstr)
# %%
import csv, os
a = open('file_op.txt', mode='r')
fstr = a.read()
print(fstr)

# %%
with open('hrdata.csv', mode=str('r')) as csv_r:
    readcsv = csv_r.read()
    print(readcsv)
# %%
f = open("file_op.txt", "a")
number = str(input("Podaj nr podpunktu"))
values = str(input("Podaj zawartośc punktu"))
f.write(f", {number}. {values}")
# f = open("file_op2.txt", "w") - Tworzy nowy plik jak nie istnieje
f = open("file_op.txt", "rt")
print(f.read())
f.close()
# %%
import os
opcion = "1: open, 2: find, 3: explore, 4: edit, 5: print"
operated = int(input(f"Podaj nr operacji {opcion}"))
listed = range(1,6)
for x in listed:
    if operated != x:
        operated
    else:
        if operated ==1:
            os.startfile('file_op.txt', operation='open')
        if operated ==2:
            os.startfile('file_op.txt', operation='find')
        if operated ==3:
            os.startfile('file_op.txt', operation='explore')
        if operated ==4:
            os.startfile('file_op.txt', operation='edit')
        if operated ==5:
            os.startfile('file_op.txt', operation='print')
        else:
            operated
# %%
# %%
a = [1,6]
b = 5
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])
# %%
