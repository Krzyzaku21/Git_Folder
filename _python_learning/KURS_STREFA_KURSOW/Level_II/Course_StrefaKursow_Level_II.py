#%%
#TODO stringi
# one_line_string = "tekst\tjednej\tlinii"
# two_line_string = """
# text
# text
# text
# """
# print("%s" % one_line_string)
# print("%s" % two_line_string)
# print(f"first\n{one_line_string}""\n"f"\nsecond{two_line_string}")

# def myArg(*args):
#     for arg in args:
#         print(f'{arg};')
# myArg(1,2,3,4,5)

# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print ("%s == %s" %(key, value))
# myFun(first ='Geeks', mid ='for', last='Geeks')
#%%
#TODO while
# wartosc = 0
# while wartosc < 10:
#     print("nieskończonosc")
#     wartosc += 1
#     exit()

# count = 0
# while count < 100:
#     if count % 50 == 0:
#         count += 1
#         continue
#     if count % 20 == 0:
#         break
#     print("Nasze liczby: {}".format(count))
#     count +=1
# print("Koniec pętli")
#%%
#TODO pętla for
# colors = ['blue', 'green', 12, 'all']
# for color_type in colors:
#     if color_type == 'blue':
#         print(f'best {color_type}')
#     if color_type == 'green':
#         print(f' {color_type} ')
#         continue
#     if type(color_type) == type(int()):
#         break
#%%
#TODO operatory logiczne
# name = "AA"
# surname = "BB"
# name_unknown = name or "NN"
# surname_unknown = surname or "NN"
# if not name:
#     print("nasz gosc nie ma imienia.")
# if name or surname:
#     print(f"Imie : {name} , Nazwisko {surname}")
#     print("logiczna wartosc dla imie {} logiczna dlanazwisko {}".format(bool(name),
# bool(surname)))
# else:
#     print("Nie ma imienia {} i nazwiska {}".format(name_unknown, surname_unknown))

#%%
#TODO imput uzytkownika
# shop_shelf = ["Apple", "Orange", "Bread", "Milk"]
# basket = []
# goods = len(shop_shelf) -1
# print(goods)
# print("In our store:")
# for assortyment in shop_shelf:
#     print(assortyment, end=", ")
# waching_goods = 0
# while waching_goods <= goods:
#     print("\n You take it in hand: {}".format(shop_shelf[waching_goods]))
#     decision = input("Do you want to put this product in the basket: ")
#     if decision == "YES":
#         basket.append(shop_shelf[waching_goods])
#         shop_shelf[waching_goods] = ""
#     waching_goods += 1
# print("In your basket:")
# for in_basket in basket:
#     print(in_basket, end=", ")
# print("\nIn our assortyment:")
# for assortyment in shop_shelf:
#     print(assortyment, end=", ")
# print("")

#%%
#TODO używanie funkcji w skryptach
# def shopping(section =[]):
#     goods = len(section)
#     basket =[]
#     watching_goods = 0
#     while watching_goods < goods:
#         print("\n You take it in hand: {}".format(section[watching_goods]))
#         decision = input("Do you want to put this product in the basket: ")
#         if decision == "YES":
#             basket.append(section[watching_goods])
#             section[watching_goods] = ""
#         watching_goods += 1
#     return basket
# def cash_register(*argv):
#     if cash_register is not None:
#         for arg in argv:
#             for good in arg:
#                 print(good, end=", ")
#     print("")
# shop_shelf1 = ["Apple", "Orange", "Banana", "Kiwi", "Pear"]
# shop_shelf2 = ["Toy Car", "Toy Helicopter", "Toy Train"]
# basket1 = shopping(shop_shelf1)
# basket2 = shopping(shop_shelf2)
# cash_register(basket1, basket2)

#%%
#TODO bibloteki, praca z plikami i zmienne srodowiskowe
# import time, os
# # odczyt z plików
# def readFromFile(*path_to_files):
#     if path_to_files is not None:
#         for path in path_to_files:
#             server_file = open(path, 'r')
#             server_configuracion = server_file.read()
#         print(server_configuracion)
#         server_file.close()
# def writeToFile(*path_to_files):
#     if path_to_files is not None:
#         for path in path_to_files:
#             server_file = open(path, 'w')
#             title = "DEVELOPER MODE\n"
#             server_file.write(title)
#             server_params = [ "CPU=20\n", "RAM=30G\n", "TOTALDISK=3\n", "\t/dev/sda, /dev/sdb, /dev/sdc\n"  ]
#             server_file.write(''.join(server_params))
#         server_file.close()
# #wykonanie operacji czas
# start_time = time.localtime()
# print("Script start time: {}:{}:{} ".format(start_time.tm_hour,start_time.tm_min, start_time.tm_sec))
# #server
# stage = os.getenv("STAGE", default="dev".upper())
# if stage.startswith("PROD"):
#     output = f"SERVER is in {stage} mode"
#     print(output)
#     exit()
# elif os.path.exists("./_python_learning\KURS_STREFA_KURSOW\Level_II\server.conf"):
#     readFromFile("./_python_learning\KURS_STREFA_KURSOW\Level_II\server.conf")
# else:
#     writeToFile("./_python_learning\KURS_STREFA_KURSOW\Level_II\server.conf")
# #wykonanie operacji czas
# stop_time = time.localtime()
# difference = time.mktime(stop_time) - time.mktime(start_time)
# print(f" Script stop time : {time.strftime('%X', stop_time)}")
# print("Total time: {} secounds".format(difference))

# %%
# # TODO Parametry command line
# import time, os , sys
# #odwozwanie sie i pryekayzwnaie argumentw do nasyego skrzptu
# #przekazanie zmiennej path_from zawierającą artykuły argv do skryptu za pomocą modułu sys
# path_from = sys.argv[1] #index0 - to nazwa anszego skryptu, index1 - to dopiero pierwszy argument zmiennej

# # odczyt z plików
# def readFromFile(*path_to_files):
#     if path_to_files is not None:
#         for path in path_to_files:
#             server_file = open(path, 'r')
#             server_configuration = server_file.read()
#         print(server_configuration)
#         server_file.close()
# # zapis do plików
# def writeToFile(*path_to_files):
#     if path_to_files is not None:
#         for path in  path_to_files:
#             server_file = open(path, 'w')
#             title = "DEVELOPER MODE\n"
#             server_file.write(title)
#             server_params = [ "CPU=20\n", "RAM=30G\n", "TOTALDISK=3\n", "\t/dev/sda, /dev/sdb, /dev/sdc\n"  ]
#             server_file.write(''.join(server_params))
#         server_file.close()
# #wykonanie operacji czas
# start_time = time.localtime()
# print("Script start time: {}:{}:{} ".format(start_time.tm_hour,start_time.tm_min, start_time.tm_sec))
# #server
# stage = os.getenv("STAGE", default="dev").upper()
# if stage.startswith("PROD"):
#     output = f"SERVER is in {stage} mode"
#     print(output)
#     exit()
# elif os.path.exists(path_from):
#     readFromFile(path_from)
# else:
#     writeToFile(path_from)
# #wykonanie operacji czas
# stop_time = time.localtime()
# difference = time.mktime(stop_time) - time.mktime(start_time)
# print("Script stopped at : {}".format(time.strftime('%X',stop_time)))
# print("Total time: {} secounds".format(difference))

#wywołanie w terminalu : python Course_StrefaKursow_Level_II.py "./server.conf"
# %%
#import własnego modułu folder Lession5_5
# %%
#TODO argparse - moduł 
#przekazywanie zmiennych do naszego sryptu przy pomocy modułu "argparse" (daje help, daje typ kompilacji)
# import time, os, sys, argparse

# #path_from = sys.argv[1]

# def readFromFile(*path_to_files):
#     if path_to_files is not None:
#         for path in path_to_files:
#             server_file = open(path, 'r')
#             server_configuration = server_file.read()
#         print(server_configuration)
#         server_file.close()

# def writeToFile(*path_to_files):
#     if path_to_files is not None:
#         for path in  path_to_files:
#             server_file = open(path, 'w')
#             title = "DEVELOPER MODE\n"
#             server_file.write(title)
#             server_params = [ "CPU=20\n", "RAM=30G\n", "TOTALDISK=3\n", "\t/dev/sda, /dev/sdb, /dev/sdc\n"  ]
#             server_file.write(''.join(server_params))
#         server_file.close()

# #funkcja argparse dająca skrypt do pliku path_from za pomocą modułu results.path_from, wraz z danymi help i kompilatora
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-f', '--file', action='store', dest='path_from', default='./server.conf', help='Path to your file')

#     results = parser.parse_args()

#     start_time = time.localtime()
#     print("Script start time: {}:{}:{} ".format(start_time.tm_hour,start_time.tm_min, start_time.tm_sec))

#     stage = os.getenv("STAGE", default="dev").upper()

#     if stage.startswith("PROD"):
#         output = f"SERVER is in {stage} mode"
#         print(output)
#         exit()
#     elif os.path.exists(results.path_from):
#         readFromFile(results.path_from)
#     else:
#         writeToFile(results.path_from)

#     stop_time = time.localtime()
#     difference = time.mktime(stop_time) - time.mktime(start_time)
#     print("Script stopped at : {}".format(time.strftime('%X',stop_time)))
#     print("Total time: {} secounds".format(difference))

# if __name__ == '__main__':
#     main()

# %%
#TODO handling try/except/else/finally, except: #jeżeli wyskoczy błąd to wyświetli informacje jak używać tego skryptu
#finally - zawsze wykonywana

# import time, os, sys

# #path_from = sys.argv[1]

# def readFromFile(*path_to_files):
#     if path_to_files is not None:
#         for path in path_to_files:
#             server_file = open(path, 'r')
#             server_configuration = server_file.read()
#         print(server_configuration)
#         server_file.close()

# def writeToFile(*path_to_files):
#     if path_to_files is not None:
#         for path in  path_to_files:
#             server_file = open(path, 'w')
#             title = "DEVELOPER MODE\n"
#             server_file.write(title)
#             server_params = [ "CPU=20\n", "RAM=30G\n", "TOTALDISK=3\n", "\t/dev/sda, /dev/sdb, /dev/sdc\n"  ]
#             server_file.write(''.join(server_params))
#         server_file.close()
# try:
#     path_from = sys.argv[1]
# except:
#     print(f"Usage: {sys.argv[0]} \"./path_to_your_file\"")
# else:
#     start_time = time.localtime()
#     print("Script start time: {}:{}:{} ".format(start_time.tm_hour,start_time.tm_min, start_time.tm_sec))

#     stage = os.getenv("STAGE", default="dev").upper()

#     if stage.startswith("PROD"):
#         output = f"SERVER is in {stage} mode"
#         print(output)
#         exit()
#     elif os.path.exists(path_from):
#         readFromFile(path_from)
#     else:
#         writeToFile(path_from)

#     stop_time = time.localtime()
#     difference = time.mktime(stop_time) - time.mktime(start_time)
#     print("Script stopped at : {}".format(time.strftime('%X',stop_time)))
#     print("Total time: {} secounds".format(difference))

# %%
#TODO wykonywanie poleceń powłoki w python
# powłoka zewnetrzna windows cmd, powershella, czy linux bash

# import subprocess

# run_shell = subprocess.run(['ls', './echo'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# test = str(run_shell.stdout.decode()).split('\n')

# for el in test:
#     if not el:
#         continue
#     print(f"Plik: {el}")
# print("Info: {}".format(run_shell.stderr.decode()))

# %%
#TODO Zaawansowana iteracja ze zrozumieniem list

# import argparse

# parser = argparse.ArgumentParser(description='Szukanie wedlug klucza')
# parser.add_argument('snippet', help='czesc lub cale slowo')

# args = parser.parse_args()
# snippet = args.snippet.lower()

# words = open('/usr/share/dict/polish').readlines()
# print([word.strip() for word in words if snippet in word.lower()])
#python3 Course_StrefaKursow_Level_II.py basia
# %%
#TODO random and json
# import random
# import json

# count = 10
# words = [word.strip() for word in open('words').readlines()]

# for id in range(count):
#     amount = random.uniform(1.0, 1500)
#     content = {
#             'topic': random.choice(words),
#             'value': "%.2f" % amount
#             }
#     with open(f'./receipts/receipt-{id}.json','w') as f:
#         json.dump(content, f)
# %%
# TODO shutil and glob
# import glob # odczyt wielu plików na raz
# import os # wprowadzanie funkcji terminala do pythona
# import shutil #przenoszenie plików
# import json

# try:
#     os.mkdir("./processed")
# except OSError:
#     print("'./processed' directory already exists")

# receipts = glob.glob('./receipts/receipt-[0-9]*.json')
# subtotal = 0.0

# for path in receipts:
#     with open(path) as f:
#         content = json.load(f)
#         subtotal += float(content['value'])
#     name = path.split('/')[-1]
#     destination = f"./processed/{name}"
#     shutil.move(path, destination)
#     print(f"moved '{path}' to '{destination}'")

# print("Receipt subtotal: $%.2f" % subtotal)
# %%
#TODO re and math
##podsumowanie tylko dla rachunków parzystych
# import glob # odczyt wielu plików na raz
# import os # wprowadzanie funkcji terminala do pythona
# import shutil #przenoszenie plików
# import json
# import re #sprawdzanie zapisu czy się zgadza

# try:
#     os.mkdir("./processed")
# except OSError:
#     print("'./processed' directory already exists")

# receipts = [f for f in glob.glob('./receipts/receipt-[0-9]*.json') if re.match('./receipts/receipt-[0-9]*[02468].json', f)]
# subtotal = 0.0

# for path in receipts:
#     with open(path) as f:
#         content = json.load(f)
#         subtotal += float(content['value'])
#     destination = path.replace('receipts','processed')
#     shutil.move(path, destination)
#     print(f"moved '{path}' to '{destination}'")

# print("Receipt subtotal: $%.2f" % subtotal)
# %%
# TODO - Pola klasy
# class Car:
#     def __init__(self, model, brand, vinnumber): #funkcja inicjująca klasę Car
#         self.model = model
#         self.brand = brand
#         self.vinnumber = vinnumber

#     def print_information(self): #funkcja wykorzystująca wartości klasy Car
#         print("My car is:", self.model)
#         print("My car brand is:", self.brand)
#         print("My car vin is:", self.vinnumber)

# myCar1 = Car("126p", "Fiat", "817349tfdc") #tworzenie danych klasy Car
# myCar2 = Car("125p", "Fiat", "gfcb89b28f")

# myCar1.print_information() #uruchamianie funkcji klasy Car
# myCar2.print_information()
# %%
#TODO Hermatyzacja - pola są ukryte i nie nadpisujemy ich, tylko odpowiednio z nich metodami settery i gettery
# pliki Car and hermetyzacja

# %%
#TODO Porównywanie obiektów z plikiem porownainie.py
class Person:
    def __init__(self, name, surname, nickname):
        self.name = name
        self.surname = surname
        self.nickname = nickname

    def printPersonInformation(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Nickname: {self.nickname}")
# %%
#TODO Kółko krzyżyk klasa
#folder tictac1 -> board.py

# %%
# %%
# %%
