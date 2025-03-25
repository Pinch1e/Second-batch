#List Comprehension
from IPython.terminal.interactiveshell import black_reformat_handler
from pygments.styles.dracula import yellow

fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits]
print(newlist)

#Tuple
thisti = ("cherry",)
print(type(thisti))
#the comma differentiates a str from a tuple

#Unpacking Tuples
fruits = ("cherry", "grape", "blackcurrant")
(green, yellow, black) = fruits
print(green)
print(yellow)
print(black)