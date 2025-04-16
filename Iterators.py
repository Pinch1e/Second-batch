#The iterators like the name goes through all the numbers in an object

myguy = ("apple", "Banana", "guava")
myit = iter(myguy)

print(next(myit))
print(next(myit))

#Looping through an iterator
class JamboNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

baba = JamboNumbers()
lowkey = iter(baba)

print(next(lowkey))
print(next(lowkey))
print(next(lowkey))
print(next(lowkey))
print(next(lowkey))
print(next(lowkey))
print(next(lowkey))
