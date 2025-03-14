class Worker:
    def __init__(self,name,salary,years):
        self.name=name
        self.salary=salary
        self.years=years
    def pension(self):
        return .10 * self.years * self.salary
    def getname(self):
        return self.name

class Manager(Worker):
    def __init__(self,name,salary,years):
        super().__init__(name,salary,years)
    def pension(self):
        return .20 * self.years * self.salary

class Executive(Manager):
    def __init__(self,name,salary,years):
        super().__init__(name,salary,years)
    def pension(self):
        return .30 * self.years * self.salary


e1 = Worker("Bob",20000,3)
e2 = Manager("Sally",30000,2)
e3 = Executive("Alice",50000,1)

emps = [e1, e2, e3]
for e in emps:
    print("{}'s pension is worth ${:,.2f}".format(e.getname(),e.pension()))
