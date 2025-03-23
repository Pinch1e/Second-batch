#Opening a File
from numpy.lib.format import open_memmap

f = open("pinchie.txt")
print(f.read())

#Read only parts of the file
f = open("pinchie.txt")
print(f.read(4))

#Read Lines
f = open("pinchie.txt")
print(f.readline())
f.close()

#Append
f = open("pinchie.txt", "a")
f.write("Now the files has more content")
f.close()

print(f)

#Check if the file exists
import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("This File does not exist")

#Remove a File
import os
os.remove("pinchie.txt")

