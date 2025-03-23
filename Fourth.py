#Opening a File
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