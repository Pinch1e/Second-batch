#Creating a function
#In Python a function is defined using the def keyword

def my_function():
    print("Hello from a function")

#Arguments
def ppa(dname):
    print(dname + " Dagbana")

ppa("Email")
ppa("Arsenal")
ppa("Bosch")

#Arbitrary Arguments
def my_kids(*kids):
    print("The youngest child is " + kids[2])

my_kids("Me", "You", "Them")