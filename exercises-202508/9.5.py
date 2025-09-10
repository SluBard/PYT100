class Worker:
    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years
    def pension(self):
        return self.salary*.1
    def getname(self):
        return self.name

class Manager(Worker):
    def __init__(self,name,salary,years):
        super().__init__(name,salary,years)
    def pension(self):
        return self.salary*.2

class Executive(Manager):
    def __init__(self,name,salary,years):
        super().__init__(name,salary,years)
    def pension(self):
        return self.salary*.3

emp1 = Worker("Joe", 30000, 15)
emp2 = Manager("Sue", 40000, 5)
emp3 = Executive("Alice", 50000, 10)

emps = [emp1, emp2, emp3]
for emp in emps:
    print("{}'s pension is worth ${:,.2f}".format(emp.getname(),emp.pension()))
