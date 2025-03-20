#Upper Case
a = "Hello, World!"
print(a.upper())

#Lower Caase
a = "Hello World"
print(a.lower())

#Remove Whitespaces
a = " Hello, World! "
print(a.strip())

#Replace String
a = "Hello String "
print(a.replace("H", "J"))

#Place holders
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Escape Character
txt = "We are the so called \"Vikings\" from the north"
print(txt)

#Len
x = "banana"
print(len(x))

#Question 1
x = "The best things in life are free"
if "free" in x :
    print(True)