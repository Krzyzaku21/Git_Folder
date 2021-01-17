# ZAD1
# metoda ".format" wstawia dane w tekst
def met_format1():
    produkt = 12
    s = "W magazynie {} {} sztuk.".format(produkt, produkt)
    print(s)


def met_format2():
    tekst = "KOT"
    wstawiam = "PIES"
    s = f"Losowy {tekst} tutaj {wstawiam}"
    print(s)


# ZAD2
# metoda ".title" zwraca tekst zapisany z wielkich liter


def met_title1():
    zmieniony_tekst = str(input("Podaj jakiś tekst: "))
    zmieniony_tekst2 = zmieniony_tekst.title()
    tekst2 = print("Twój nowy tekst z wielkiej litery to: " + zmieniony_tekst2)


# ZAD3
# metoda ".replace" - zmienia dany tekst lub słowo w inne


def met_replace1():
    print("Zamień jedno ze słów w tym zdaniu")
    zmieniony_tekst = "Zamień jedno ze słów w tym zdaniu"
    pierwsze_slowo = str(input("Podaj słowo z podanego powyżej tekstu do zmiany: "))
    drugie_slowo = str(input("Podaj jakiś tekst: "))
    print(
        "Twój zmieniony tekst to: "
        + zmieniony_tekst.replace(pierwsze_slowo, drugie_slowo)
    )


# ZAD4
# metoda ".upper" - zamienia cały tekst na drukowane litery


def met_upper1():
    tekst = str(input("Napisz co kolwiek a będzie drukowane: "))
    print(tekst.upper())


# ZAD5


word = "Hello World"
print(word[1])
