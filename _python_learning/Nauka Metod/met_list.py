# my_list = []
# 1. Zbiór wartości, 2. indeks od 0
# 3. Łatwe : dodawanie, odczytywanie, usówanie wartości, 4. Lista posiada swój indeks
# 5. Comprehension [expression for item in list] - 
def list_comprehension():
    point1 = "lista liter ze słowa human"
    point2 = "lista z mapowaniem funkcji lambda i lista2 z filtrowaniem funkcji lambda "
    point3 = "zaleznosci if w list comprehension"
    point4 = "lista liter ze słowa human"
    print(f'1: {point1}\n',f'2: {point2}\n',f'3: {point3}\n',f'4: {point4}\n')
    points=int(input("Podaj wartość od 1 do 4: "))
    if points == 1:
        h_letters = [ letter for letter in 'human' ]
        print( h_letters)
    elif points == 2:
        print('Mapowanie')
        my_list = [1, 5, 4, 6, 8, 11, 3, 12]
        new_list = list(map(lambda x: x * 2 , my_list))
        print(new_list)
        print('Filtrowanie')
        my_list = [1, 5, 4, 6, 8, 11, 3, 12]
        new_list = list(filter(lambda x: (x%2 == 0) , my_list))
        print(new_list)
    elif points == 3:
        num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
        print(num_list)
    else:
        obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
        print(obj)
#ZAD1
#metoda ".count" - pregląda listę i zwraca ilość tych samych argumenów, zwraca int
def list_count1():
    lista =['dupa', '1', 1, 3.0, 'dupa', True, False, None, 1, 'dupa', "dwa", "dwa", 2, 2]
    print(lista)
    print(lista.count((input('Podaj jeden ze znaków z listy powyżej: '))))
#ZAD2
#metoda ".sorted" - sortuje liczby 
def list_sorted1():
    lista =[4,3,5,6,9,1,2,33,65,32,41,98,102]
    lista2 = lista.copy()
    sortowanie = sorted(lista, reverse=True)
    sortowanie2 = sorted(lista, reverse=False)
    print('Posortowana dana liczba: ',lista2)
    print(sortowanie, " : reverse - odwrotnie True")
    print(sortowanie2)
#ZAD2
#metoda ".sort" - sortuje liczby jak w sorted
def list_sorted2(lista):
    print('Posortowana dana liczba: ',*lista)
    lista.sort()
    print("Wynik: ",', '.join(str(x) for x in lista))
    lista.reverse()
    print("Wynik liczby odwrotnie: ",', '.join(str(x) for x in lista))

#ZAD3 
#metody typu sort() a sorted(), reverse() a reversed()
#różnią się tym, iż metody sort, reverse działają na jednym obiekcie (bez kopii),
#natomiast funkcje sorted, reversed mogą być uzywane wiele razy i tworzą nowe obiekty
def list_difference_sort_sorted():
    numbers = [6, 9, 3, 1]
    print(id(numbers), numbers)
    num2 = [6, 9, 3, 1]
    #num2 = numbers.copy()
    print(id(num2), num2)
    num1 = sorted(numbers)
    num2.sort()

def list_append1(my_list):
    Limit = (len(my_list))
    for v in range(0,Limit+1):
        if v == Limit:
            my_list[4] = 20 #zmienia wartość 'True' na 4 pozycji na '20'
            my_list.append(5) #dokleja wartość na końcu listy na obiekcie
            my_list2 = [3, 20]
            my_list = my_list + my_list2
            print("First list: ",my_list)
            print("Is number 5 in frist list? :",5 in my_list)
    my_list3 = [v for v in range(9, 27) if v % 2 == 0 ] #wartosci spełniajace wartosci parzyste tylko wypisze
    print("Second list: ",my_list3)

def One_ListValues_to_SecondListValues( list1, list2 ):
    score = [x for x in range(0,len(list1))]
    for a in score:
        print(list1[a], list2[a])
# list1 = ["red", "big", "tasty"]
# list2 = ["apple", "banana", "cherry"]
# One_ListValues_to_SecondListValues(list1, list2) 

def ListEnumerate(list1, list2):
    for i, (list1_v) in enumerate(list1):
        print(i, list1_v, list2[i])
persons =["adam", "wojtek"]
adres = ["nike", "słowackiego"]
# ListEnumerate(persons, adres)


def test_zip( foo, bar ):
    store = []
    for f, b in zip(foo, bar):
        store.append( (f, b) ) 
        print(f,b)
# test_zip(persons, adres)