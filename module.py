import module_test

module_test.greetings("Jonathan")

a = module_test.person1["age"]
print(a)

#Renaming the Module
import module_test as papi
a = papi.person1["age"]
print(a)
b = papi.person1["name"]
print(b)
c = papi.person1["country"]
print(c)

#Built in Modules
import platform
x = platform.system()
print(x)

import platform
x = dir(platform)

f = open("Dates.py", "x")
