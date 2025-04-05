#Sets
thisset = {"Dragon", "Elephant", "Pawpaw"}
thisset.add("Paradwy")
print(thisset)

#Updating a Set
tropical = {"Arsenal", "Drew", "Deter"}
thisset.update(tropical)
print(thisset)

#Removing a Set
thisset.remove("Paradwy")
print(thisset)

#Or Usind the discard
thisset.discard("Deter")
print(thisset)

#The clear() clears a Set and the del() deletes a Set
#Loop Sets
for x in thisset:
    print(x)

f = open("Tenth.py", "x")