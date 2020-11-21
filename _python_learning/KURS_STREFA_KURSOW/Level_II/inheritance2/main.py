from board import *

kwadrat = Square(15)
prostokąt = Rectangle(10, 20)
romb = Rhombus(3, 3.7)

slownik = {
    'kwadrat' : kwadrat,
    'prostokąt' : prostokąt,
    'romb' : romb,
}

for key, figura in slownik.items():
    amount = figura.area()
    print(f"Pole {key} wynosi: ", "%.1f" % amount)
    print(f"Obwód {key} wynosi: ", figura.perimeter())
