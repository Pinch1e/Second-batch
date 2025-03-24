#Creating a new Folder
import os
Sabi = "New_folder"
os.makedirs("new_folder", exist_ok=True)
print(f"Folder '{"sab"}' created successfully!")

#List Comprehension
Panther = ["Batiboy", "Juvenile", "Dada", "Dracula"]
newlist = []
for x in Panther:
    if "e" in x:
        print(newlist.append(x))

print(newlist)

#Sort LIst
numero = [25, 36, 45, 89, 100]
numero.sort()
print(numero)

#Sort Descending
thislist = ["Cherrry","Banana", "dracula", "Porter"]
thislist.sort(reverse=True)
print(thislist)