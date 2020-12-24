class Worker:
    def __init__(self,name,salary,years):
        self.name = name
        self.salary = salary
        self.years = years
    def pension(self):
        return self.years * self.salary * .1
    def getname(self):
        return self.name

class Manager(Worker):
    def pension(self):
        return self.years * self.salary * .2

class Executive(Manager):
    def pension(self):
        return self.years * self.salary * .3

w = Worker("Bob",50000,5)
m = Manager("Joe",70000,10)
e = Executive("John",90000,20)

mylist = [ w, m, e]

for emp in mylist:
    print("{} has a pension of {:5,.2f}".format(emp.getname(),emp.pension()))
