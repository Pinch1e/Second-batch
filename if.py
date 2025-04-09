#IF / ELSE STATEMNENT IN PYTHON
#a == b Equals
#a != b Not Equals

a = 33
b = 242
if b > a :
    print("b is greater than a")

#Elif Condition
a = 33
b = 33
if b > a :
    print("b is greater than a")
elif b == a :
    print("b and a are equal")
else :
    print("a is greater than b")

#One line statement
if a > b: ("print a is greater than b")

#Match
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
