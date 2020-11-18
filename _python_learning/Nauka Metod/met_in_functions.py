#ARGUMENTY prekazywanie
def fn_argumenty(a, b, *args, **dict_args):
    #a, b - argumenty int
    #*args - argumenty typu tuple
    #**dict_args - argumenty dictionary
    for i in a, b:
        print(i)
    for arg in args:
        print(arg)
    for key in dict_args:
        print(dict_args[key]) 
#ZWRACANIE W RETURN
def fn_return(a,b):
    return a + b, a * b, a - b #wraca tuple
#DZIEDZICZENIE MIĘDZY FUNKCJAMI
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
def apply(fn, a, b):
    return fn(a, b)
#DZIEDZICZENIE MIĘDZY FUNKCJAMI

#ZAD1
#funkcja "abs()" - liczba dodatnia z działania
def fun_abs():
    for x in range(-10,-5):
        x = abs(x)
        print(x)
    for y in range (-20,-15):
    #abs dla liczby zespolonej a+bi wzór to: |z|=pierwiastek(a**2+b**2)
        x +=1j
        print(y)
#ZAD2
#funkcja "all()" - zwraca True jeśli wszystkie wartości są prawdziwe (1, True), dla dictionary sprawdza klucze
def fun_all():
    list1 = [1, True, 1, 1, 1, 23, 45, -2]
    print(all(list1))
    tuple1 = (-1, 1, False, 0)
    print(all(tuple1))
    myset1 = {0, 1, 0}
    print(all(myset1))
    mydict = {0 : "Apple", 1 : "Orange"}
    print(all(mydict))
#ZAD3
#funkcja "any()" - jesli chociaż jedna jest prawdziwa to zwraca True
def fun_any():
    myset1 = {0, 1, 0}
    print(any(myset1)) 
#ZAD4
#funkcja "compile()" - zamienia plik typu string, lub AST na plik typu Obiekt
def fun_compile(a, b):
    codeInString = 'a\nb\nsum=a+b\nprint("sum =",sum)'
    codeObejct = compile(codeInString, 'sumstring', 'exec')
    exec(codeObejct)