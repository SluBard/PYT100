#!/usr/bin/env python3
#
# A Solution For Chapter 9 Exercise 2
#
class Person:
    def __init__(self, fn = "Default", age = 21, sex = "Default"):
        self.name = fn
        self.age = age
        self.sex = sex

	def __str__(self):
        s = self.name + " "
        s += str(self.age) + " "
        s += self.sex
        return s

class Family:
    def __init__(self, m, d, *args):
        self.mom = m
        self.dad = d
        self.kids = []
        for i in args:
            self.kids.append(i)

    def add(self, kid):
        self.kids.append(kid)

    def __str__(self):
        s = str(self.mom) + " " + str(self.dad) 
        for i in self.kids:
            s += "\n\t" + str(i)
        return s

mom = Person("Sally", 76, "F") 
dad = Person("Arthur", 62, "M")
print(mom)
print(dad)

joe = Person("Joel", 41, "M")
judy = Person("Judy", 38, "F");
fam = Family(mom, dad, joe, judy) 
print("*** Family Members are")
print(fam)
print("*** End Family Members")

mike = Person("Michael", 33, "M")
fam.add(mike)
print("*** Family Members are")
print(fam)
print("*** End Family Members")
