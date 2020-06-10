class Square:  # public
    def __init__(self, sides):
        self.sides = sides


class Triangle:  # public
    def __init__(self, sides):
        self.sides = sides


class Reactangle:  # protected
    _sides = None

    def __init__(self, sides):
        self._sides = sides

    def display(self):
        print("sides:", self._sides)


class Pentagon:  # protected
    _sides = None

    def __init__(self, sides):
        self._sides = sides

    def display(self):
        print("sides:", self._sides)


class Hexagon:  # protected
    _sides = None

    def __init__(self, sides):
        self._sides = sides

    def display(self):
        print("sides:", self._sides)


class Heptagon:  # protected
    _sides = None

    def __init__(self, sides):
        self._sides = sides

    def display(self):
        print("sides:", self._sides)


class Octagon:  # public
    def __init__(self, sides):
        self.sides = sides


class Decagon:  # private
    __sides = None

    def __init__(self, sides):
        self.__sides = sides

    def display(self):
        print("sides:", self.__sides)


class Nonagon:  # private
    __sides = None

    def __init__(self, sides):
        self.__sides = sides

    def display(self):
        print("sides:", self.__sides)


class Triskaidecagon:  # private
    __sides = None

    def __init__(self, sides):
        self.__sides = sides

    def display(self):
        print("sides:", self.__sides)


sam = Square(4)
print('Square')
print(sam.sides)
sam.sides = 5
print('Square')
print(sam.sides)
frank = Triangle(3)
print('Triangle')
print(frank.sides)
frank.sides = 3
print(frank.sides)
print('Reactangle')
turk = Reactangle(4)
turk.display()
print('Pentagon')
tyler = Pentagon(5)
tyler.display()
print('Hexagon')
haley = Hexagon(6)
haley.display()
print('Heptagon')
p = Heptagon(7)
p.display()
print('Octagon')
ch = Octagon(8)
print(ch.sides)
print('Decagon')
hr = Decagon(10)
hr.display()
print('Nonagon')
ol = Nonagon(9)
ol.display()
print('Triskaidecagon')
dr = Triskaidecagon(13)
dr.display()
