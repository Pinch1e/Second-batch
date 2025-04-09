#IF / ELSE STATEMNENT IN PYTHON
#a == b Equals
#a != b Not Equals
from calendar import weekday

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

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

#Combine values
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")