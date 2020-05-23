class Shape:
    def __init__(self):    # Constructor of the class
        print("Shape created")

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self):
        Shape.__init__(self)
        print("Circle created")

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi



    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2
class Triangle(Shape):
    def __init__(self):
        Shape.__init__(self)
        print("Triangle created")
    def setSides(self,a,b,c):
        self.a =a
        self.b =b
        self.c =c
        self.perimeter = self.a + self.b + self.c

    def getPerimemeter(self):
        return self.perimeter


class Square(Shape):
    def __init__(self):
        Shape.__init__(self)
        print("Square created")

    def setSides(self, side):
        self.side = side
        self.perimeter = 4 * self.side

    def getPerimemeter(self):
        return self.perimeter


class Rectangle(Shape):
    def __init__(self):
        Shape.__init__(self)
        print("Rectangle created")

    def setSides(self, a, b, c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.perimeter = self.a + self.b + self.c+self.d

    def getPerimemeter(self):
        return self.perimeter
class Pentagon(Shape):
    def __init__(self):
        Shape.__init__(self)
        print("Pentagone created")

    def setSides(self, a, b, c, d,e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e =e

        self.perimeter = self.a + self.b + self.c + self.d+ self.e

    def getPerimemeter(self):
        return self.perimeter

class Hexagon(Shape):
    def __init__(self):
        Shape.__init__(self)
        print("Hexagon created")

    def setSides(self, a, b, c, d, e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

        self.perimeter = self.a + self.b + self.c + self.d + self.e + self.f

    def getPerimemeter(self):
        return self.perimeter


class Heptagon(Shape):
    def __init__(self):
        Shape.__init__(self)
        print("Heptagon created")

    def setSides(self, a, b, c, d, e, f,g):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g =g


        self.perimeter = self.a + self.b + self.c + self.d + self.e+ self.f + self.g

    def getPerimemeter(self):
        return self.perimeter

class Octagon(Shape):
    def __init__(self):
        Shape.__init__(self)
        print("Octagon created")

    def setSides(self,  a, b, c, d, e, f,g,h) :
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h=h

        self.perimeter = self.a + self.b + self.c + self.d + self.e+ self.f + self.g + self.h

    def getPerimemeter(self):
        return self.perimeter
class Nonagon(Shape):
    def __init__(self):
        Shape.__init__(self)
        print("Nonagon created")
    def setSides(self, a, b, c, d, e, f,g,h,i) :
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e =e
        self.f = f
        self.g = g
        self.h = h
        self.i = i

        self.perimeter = self.a + self.b + self.c + self.d+ self.e+ self.f + self.g + self.h + self.i


    def getPerimemeter(self):
        return self.perimeter
class Dectagon(Shape):
    def __init__(self):
        Shape.__init__(self)
        print(" Dectagon created")

    def setSides(self,a, b, c, d, e, f,g,h,i,j) :
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j

        self.perimeter = self.a + self.b + self.c + self.d + self.e+ self.f + self.g + self.h + self.i + self.j

    def getPerimemeter(self):
        return self.perimeter



c = Circle()
c.setRadius(3)
print('Circumference is: ',c.getCircumference())
t = Triangle()
t.setSides(2,3,4)
print('Perimeter is:',t.getPerimemeter())
s = Square()
s.setSides(4)
print('Perimeter is:',s.getPerimemeter())
r = Rectangle()
r.setSides(2,3,4,2)
print('Perimeter is:',r.getPerimemeter())
p = Pentagon()
p.setSides(2,3,4,2,3)
print('Perimeter is:',p.getPerimemeter())
r = Hexagon()
r.setSides(2,3,4,2,7,4)
print('Perimeter is:',r.getPerimemeter())
r = Heptagon()
r.setSides(2,3,4,2,7,4,8)
print('Perimeter is:',r.getPerimemeter())
r = Octagon()
r.setSides(2,2,3,4,2,7,4,8)
print('Perimeter is:',r.getPerimemeter())
r = Nonagon()
r.setSides(2,2,3,4,2,7,4,8,9)
print('Perimeter is:',r.getPerimemeter())
r = Dectagon()
r.setSides(2,2,3,4,2,7,4,8,9,10)
print('Perimeter is:',r.getPerimemeter())

