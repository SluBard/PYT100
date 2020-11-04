#!/usr/bin/env python3
#
# A Solution For Chapter 9 Exercise 3
#
class FamilyError(Exception):
    def __init__(self, mess):
        self.mess = mess

    def message(self):
        return self.mess

class Person:
    def __init__(self, fn, age, sex):
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
            try:
                if isinstance(i, Person):
                    self.kids.append(i)
                else:
                    raise FamilyError("in init: not a Person")
            except FamilyError as fe:
                print(fe.message())

    def add(self, kid):
        try:
            if isinstance(kid, Person):
                self.kids.append(kid)
            else:
                raise FamilyError("in add: not a Person")
        except FamilyError as fe:
            print(fe.message())

    def __str__(self):
        s = str(self.mom) + " " + str(self.dad) 
        for i in self.kids:
            s += "\n\t" + str(i)
        return s

mom = Person("Sally", 58, "F") 
dad = Person("Arthur", 54, "M")
print(mom)
print(dad)

joe = Person("Joel", 30, "M")
judy = Person("Judy", 32, "F");
x = 20
fam = Family(mom, dad, x, joe, judy)
print("*** Family Members are")
print(fam)
print("*** End Family Members")

mike = Person("Michael", 21, "M")
fam.add(mike)
print("*** Family Members are")
print(fam)
print("*** End Family Members")
fam.add(x)
