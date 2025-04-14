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

#Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Ari", child2="John", child3="Adamu")

#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:

def johndoe(**fname):
    print("Just trying my best" + fname["lname"])
johndoe(fname = "Alisson" ,lname = "Sabi")

#Default Parameter Value
def land(country = "Germany"):
    print("This is my Country  " + country)

land("Norway")
land()
land("Nigeria")
land("Finland")
land("Cartagena")

#Passing a List as an Argument
def ikeduru(lga):
    for x in lga:
        print(x)

lagos = ["apapa", "Wilmer", "Oshodi"]
ikeduru(lagos)

#Return Values
def my_function(x):
    return 10 * x

print(my_function(20))
print(my_function(10))
print(my_function(0))

f = open("lambda.py", "x")