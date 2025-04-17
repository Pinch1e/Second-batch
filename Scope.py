#A variable is only available from inside the region it is created. This is called scope.
def myFunc():
    x = 300
    print(x)

myFunc()

#A variable created outside a function is called a Global variable
x = 300

def Papi():
    x = 200
    print(x)

Papi()
print(x)

#If you use the global keyword when creating a variable , the variable belongs to the global scope
x = 300
def vamos():
    global x
    x = 400
    print(x)
vamos()
print(x)

f = open("module.py", "x")
