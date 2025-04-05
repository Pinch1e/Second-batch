#There are several ways to join two or more sets in Python.

#The union() and update() methods joins all items from both sets.

raid = {45, 34, 90}
flew = {"We", "Diablo", 56}
set3 = raid.union(flew)
print(set3)

#You can use the | operator instead of the union() method, and you will get the same result.

paraga = {"Saboteur", 45, "Hectagon"}
drag = set3 | paraga
print(drag)

f = open("Dict.py", "x")