import json

x = '{"name": "Papi", "age":35, "city": "Frankfurt"}'

y = json.loads(x)

print(y["city"]) #Converting JSON to Python

x = {
    "name" : "Pinchie",
    "age" : 35,
    "sex" : "male"
} #Python Object

y = json.dumps(x) # Cpnverting to JSON

print(y) #The result is a JSON String

#Converting Python Objects into Json Strings
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Convert Python Objects containing all legal data types
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

json.dumps(x, indent=4) #The JSON String is not easy to read and so we have to use the indent parameter to define the number of indents

json.dumps(x, indent=4, separators=(".","=")) #We use the seperator parameters to change the default parameters

json.dumps(x, indent=4, sort_keys=True) #We use the sort_key parameter to determine if the result should be sorted or not

f = open("regex.py", "x")