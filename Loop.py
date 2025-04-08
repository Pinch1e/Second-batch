#Looping through the keys and its values
x = {'type' : 'fruit', 'name' : 'apple'}
for y, z in x.items():
    print(y,z)

#Copying
y = x.copy()
print(y)

#Nested Dictionaries
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
print(customers)
print(customers['c2']['name'])

f = open("if.py", "x")