#!/usr/bin/env python3
#
# A Solution For Chapter 9 Exercise 5
#
class Worker:
    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years

    def pension(self):
        return self.years * .10 * self.salary

    def getname(self):
        return self.name

class Manager(Worker):
    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)

    def pension(self):
        return self.years * .20 * self.salary

class Executive(Manager):
    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)

    def pension(self):
        return self.years * .30 * self.salary

m = Manager("Chris", 100000, 12)
e = Executive("Susan", 100000, 7)
p = Worker("Michael", 100000, 10)

lis = [ p, m, e ]

for i, value in enumerate(lis):
    print(i, end="")
    print("\t" + str(value.pension()))
    print("\t" + value.getname())
    print()
