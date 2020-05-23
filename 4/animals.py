class Animal:
    def __init__(self):
        print("Animal created")

    def speak(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")

    def whoAmI(self):
        print("Cat")

    def speak(self):
        print("Meow!")
class Tiger(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Tiger created")

    def whoAmI(self):
        print("Tiger")

class Wolf(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Wolf created")

    def whoAmI(self):
        print("Wolf")


class Monkey(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Monkey created")

    def whoAmI(self):
        print("Monkey")

class Parrot(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Parrot created")

    def whoAmI(self):
        print("Parrot")
class Cheeta(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cheeta created")

    def whoAmI(self):
        print("Cheeta")

class Horse(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Horses created")

    def whoAmI(self):
        print("Horses")


class Owl(Animal):
    def __init__(self):
        Animal.__init__(self)
        print(" Owl created")

    def whoAmI(self):
        print(" Owl")



class Deer(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Deer created")

    def whoAmI(self):
        print("Deer")




d = Dog()
c = Cat()
d.whoAmI()
#h= Animal()#animal is a abstract class
#h.speak()#this will throw exception
d.speak()
c.whoAmI()
c.speak()
t = Tiger()
t.whoAmI()
w = Wolf()
w.whoAmI()
M = Monkey()
M.whoAmI()
p = Parrot()
p.whoAmI()
ch = Cheeta()
ch.whoAmI()
h = Horse()
h.whoAmI()
ol = Owl()
ol.whoAmI()
dr = Deer()
dr.whoAmI()

