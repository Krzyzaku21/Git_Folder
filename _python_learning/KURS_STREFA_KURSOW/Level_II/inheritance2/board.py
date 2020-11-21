
# ! klasa czworoboki
class Tetragon:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

# ! metoda obliczająca obwód
    def perimeter(self):
        return self.a + self.b + self.c + self.d
# ! metoda obliczająca pole
    def area(self):
        pass

# ! klasa prostokąt
class Rectangle(Tetragon):

    def __init__(self, a, b):
        Tetragon.__init__(self, a, b, a, b)

    def area(self):
        return self.a * self.b

# ! klasa kwadrat
class Square(Rectangle):

    def __init__(self, a):
        Rectangle.__init__(self, a, a)

# ! klasa romb
class Rhombus(Square):

    def __init__(self, a, h):
        Square.__init__(self, a)
        self.h = h

    def area(self):
        return (self.a * self.h)/2



