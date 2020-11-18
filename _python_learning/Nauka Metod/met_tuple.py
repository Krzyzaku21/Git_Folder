# my_tuple = ()
# 1. Zbiór wartości, 2. indeks od 0
# 3. Wartości nie można modyfikować!!

#Odczytywanie wartości tuple
def met_tuple_values1(values):
    new_values = values[:3]
    print(new_values)
    print((new_values + (10, 20, 30)))

#tuples prydatne operacje
#modyfikowanie wnętrza w tuple za pomocą danych w liscie
def met_list_to_tuple():
    my_list = [10, 4, 5, 17, 7, 2, 5]
    my_tuple2 = (8, 9, my_list)
    my_tuple = tuple(my_list)
    print(my_tuple)
    print(my_tuple2)
    print(sum(my_tuple)) #len - długość elementów, 
    # max - największa wartość z listy, min - najmniejsza wartosc z listy, sum - suma wartosci
    a, b, c, d, e, f, g = my_tuple #dopisywanie wartości tuple do danych
    print(a)
