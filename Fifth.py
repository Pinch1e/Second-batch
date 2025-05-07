#Create a new file
from numpy.lib.format import open_memmap

f = open("master.txt")
f = "This is a new Text file created here to see how t goes and build my basic python skills"

#AAppending a List
thislist = ["Cherry", "Winter", "Calm"]
thislist.append("Jabulani")
print(thislist)

#Extending a List
ort = [25, 30, 45]
prt = [56, 54, 78]
ort.extend(prt)
print(ort)



new_folder = open("Numpy.py", "x")