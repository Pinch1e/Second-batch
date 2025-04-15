x = lambda a : a + 10
print(x(5))

#Lambda functions can take any number of arguments
x = lambda a , b : a * b
print(x(5,6))

#Using Lambda in functions
def myfunc(n):
    return lambda a : a * n

myd = myfunc(2)

print(myd(20))

f = open("class.py", "x")