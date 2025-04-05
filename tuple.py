#tuples
from prompt_toolkit.shortcuts import input_dialog

tuples = (2, 45, 8)
for x in tuples:
    print(x)

thistuple = (56, 48, 69)
for i in range(len(thistuple)):
    print(thistuple[i])

#Joining Tuples
machine = ("great", "are", "the", "days")
jinga = machine * 2
print(jinga)

mytuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(mytuple):
  print(mytuple[i])
  i = i + 1

#True and 1 are the same values on a set
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)