class MyClass:
    x = 5

#Creating Object
p1 = MyClass
print(p1.x)

#The __init__() funtion, the init function is called autommaticaly every time the class is being used to create a new object

class Person:
    def __init__(self , name, age):
        self.name = name
        self.age = age

    def myFunc(self):
            print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myFunc()

#To Delte
del p1

#To Pass
class Person:
    pass

f = open("inheritance.py", "x")