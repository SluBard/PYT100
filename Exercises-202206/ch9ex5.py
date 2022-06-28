class Worker:
    def __init__(self,name,salary,years):
        self.name = name
        self.salary = salary
        self.years = years
    def pension(self):
        return self.salary * self.years * .1
    def getname(self):
        return self.name

class Manager(Worker):
    def __init__(self,name,salary,years):
        super().__init__(name,salary,years)
    def pension(self):
        return self.salary * self.years * .2

class Executive(Manager):
    def __init__(self,name,salary,years):
        super().__init__(name,salary,years)
    def pension(self):
        return self.salary * self.years * .3

employee1 = Worker("Bob",20000,3)
employee2 = Manager("Sally",30000,2)
employee3 = Executive("Alice",50000,1)

employees = [ employee1, employee2, employee3 ]
for employee in employees:
    print("{}'s pension is worth ${:,.2f}".format(employee.getname(),employee.pension()))