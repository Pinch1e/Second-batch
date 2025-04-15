#As the name goes , it allows you to create a class and inherit all the objects of a particular class onto another class
#There is the parent class aöso called the Base Class
#There is the child class called the Derived classs
from pyasn1_modules.rfc5280 import PersonalName


#Creating a Parent Class
# Parent Class
class Jumbo:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def mabo(self):
        print(self.name, self.sex)

# Create an instance of Jumbo
x = Jumbo("John", "Doe")
x.mabo()  # Output: John Doe

# First version of child class (inherits everything from Jumbo)
class Sabi(Jumbo):
    pass

x = Sabi("Mike", "Male")
x.mabo()  # Output: Mike Male

# Overriding __init__ in the child class to add more attributes
class Sabi(Jumbo):
    def __init__(self, name, sex, year):
        super().__init__(name, sex)  # Inherit name and sex from Jumbo
        self.grad = year            # Add a new attribute

x = Sabi("Mike", "Male", 2020)
x.mabo()             # Output: Mike Male
print(x.grad)        # Output: 2020
