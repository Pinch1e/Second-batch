#Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(len(thisdict))

#It is also possible to use the dict() constructor to make a dictionary.
pinchie_dict = dict(name = "Pinchie",  age = 45, country = "Germany")
print(pinchie_dict)

thisdict["color"] = "white"
print(thisdict)

x = thisdict.values()
print(x)

#Nested Dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}