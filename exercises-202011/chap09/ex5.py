class Worker:
    def __init__(self,name,salary,years):
        self.name = name
        self.salary = salary
        self.years = years
    def getname(self):
        return self.name
    def pension(self):
        return self.years*self.salary*.1
class Manager(Worker):
    def pension(self):
        return self.years*self.salary*.2
class Executive(Manager):
    def pension(self):
        return self.years*self.salary*.3

w1 = Worker("John",50000,20)
w2 = Manager("Bob",60000,10)
w3 = Executive("Sandra",80000,5)

for i in [w1, w2, w3]:
    print(i.getname(),i.salary,i.pension())
