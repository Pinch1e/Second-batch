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

#String Formats
price = 65
txt = "The price is {} dollars"
print(txt.format(price))

#Multiple Values
quantity = 2
itemno = 344
price = 34
txt = "i want {} pieces of itemno {} for {:.2f} dollars"
print(txt.format(quantity,itemno,price))

#Named Indexes ( Remember that to assign the variables you use = sign and not :
myorder = "i have a {carname}, it is a  {carmodel}"
print(myorder.format(carname = "Mercedes", carmodel = "E350"))
