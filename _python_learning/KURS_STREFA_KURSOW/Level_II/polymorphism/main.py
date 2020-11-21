import board as Animal

kaczka = Animal.Duck(3, 'dziwaczka')
zabawka = Animal.DuckToy('czerwony', 'metalowa')
kot = Animal.Cat()

lista = [kaczka, zabawka, kaczka, zabawka, kot]

for obiekt in lista:
    if hasattr(obiekt, 'fly'):
        obiekt.fly()
#lub
for obiekt in lista:
    try:
        obiekt.fly()
    except  AttributeError:
        print(' Obiect', obiekt, ' dont have a function fly')