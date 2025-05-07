import re #Importing the Regex - Regular Expression

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)

if x:
    print("YES! we have a match")
else:
    print("No Match")

#Some other regular expressions are
#FINDALL - Returns a list containing all matches
#SEARCH - Returns a match object if there is a match anywhere in the string
#SPLIT - Returns a list where the string has been split up in each match
#SUB - Replaces one or many matches with a string

import re
txt = "The rain in Spain"
y = re.split(r"\s", txt)
print(y)

txt = "Papi no cento"
x = re.sub("\s","9", txt) #Replacing empty space characters with 9
print(x)

import re
td = "The rain in Spain is mad"
d = re.search("ai", td)
print(d)
f = open("packages.py", "x")