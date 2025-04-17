#The word polymorphism means many forms
#One example is the lens()
class Motor:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Canoe:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail !")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

Car1 = Motor("Benz", "E350") #Create a Car Object
Canoe1 = Canoe("Umoru", "Jetsky") #Create a Canoe Object
Plane1 = Plane("Booeing", "747") #Create a Plane Object

for x in (Car1, Canoe1, Plane1):
    x.move()

#For Inheritance Class Polymorphism same process you just have to
class Car(Motor):
    pass

car2 = Car("Ford", "Mustang")

for x in (car2, Canoe1, Plane1):
    print(x.brand)
    print(x.model)
    x.move()

f = open("Scope.py", "x")