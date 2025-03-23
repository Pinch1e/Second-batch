#Python Operator
price = 59
tax = 0.39
txt =  f"The price is {price + (price * tax )} is dollars"
print(txt)

#F-Strings
def myconverter(x):
    return x * 0.3048
txt = f"The plane is flying at {myconverter(30000)} meter altitude"
print(txt)

#Using Comma as a thousand Seperator
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)