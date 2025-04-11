#The Break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    print(x)

#The Range Function
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)


for x in range(2, 30, 3):
    print(x)

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally Finished")

#Nested Loops
danga = ["a", "b", "c"]
savot = [23, 45, 7]
for x in danga:
    for y in savot:
        print(x, y)

f = open("Functios.py", "x")