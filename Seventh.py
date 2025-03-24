#Customizing Sort
def myfunc(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc )
print(thislist)

#Copying List
parara = [9, 5, 4, 89, 65]
thislist = parara.copy()
print(thislist)
print(parara)

#Joining List : There are ways to join list , either by concatenating them , Extend or append
List3 = parara + thislist
print(List3)

for  x in parara:
    thislist.append(x)

print(thislist)

[print(x) for x in ['apple', 'banana', 'cherry']]
