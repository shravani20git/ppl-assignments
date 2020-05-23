class Dog:#public
    def __init__(self, breed):
        self.breed = breed
class Cat:#public
    def __init__(self, breed):
        self.breed = breed

class Tiger:#protected
    _breed = None
    def __init__(self, breed):
        self._breed = breed
    def display(self):
        print("breed:",self._breed)
class Wolf:#protected
    _breed = None
    def __init__(self, breed):
        self._breed = breed
    def display(self):
        print("breed:",self._breed)
class Monkey:#protected
    _breed = None
    def __init__(self, breed):
        self._breed = breed
    def display(self):
        print("breed:",self._breed)
class Parrot:#protected
    _breed = None
    def __init__(self, breed):
        self._breed = breed
    def display(self):
        print("breed:",self._breed)
class  Cheetas:#public
    def __init__(self, breed):
        self.breed = breed
class Hourse:#private
    __breed = None
    def __init__(self, breed):
        self.__breed = breed
    def display(self):
        print("breed:",self.__breed)
class Owl:#private
    __breed = None
    def __init__(self, breed):
        self.__breed = breed

    def display(self):
        print("breed:",self.__breed)

class Deer :#private
    __breed = None
    def __init__(self, breed):
        self.__breed = breed
    def display(self):
        print("breed:",self.__breed)

sam = Dog(breed='Lab')
print(sam.breed)
sam.breed = 'German Shephard '
print(sam.breed)
frank = Cat('Huskie')
print(frank.breed)
frank.breed='Persian'
print(frank.breed)
turk = Tiger('Siberian')
turk.display()
tyler = Wolf('Saarloos')
tyler.display()
haley = Monkey('Baboon')
haley.display()
p = Parrot('parakeets')
p.display()
ch =Cheetas('Asiatic')
print(ch.breed)
hr = Hourse('Arabian')
hr.display()
ol = Owl('Barn Owl')
ol.display()
dr = Deer('brocket')
dr.display()