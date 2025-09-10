class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.gender
    def getname(self):
        return self.name
    def setname(self,name):
        self.name = name
    def getage(self):
        return str(self.age)
    def setage(self,age):
        self.age = age
    def getgender(self):
        return self.gender
    def setgender(self,gender):
        self.gender = gender
class Family:
    def __init__(self,mom,dad,*kids):
        self.mom = mom
        self.dad = dad
        self.kids = list()
        for kid in kids:
            self.kids.append(kid)
    def __str__(self):
        string = "{} + {}\n".format(self.mom.getname(),self.dad.getname())
        for kid in self.kids:
            string += "\t{}\n".format(kid.getname())
        return string
    def add(self,kid):
        self.kids.append(kid)
        
mom = Person("Mommy", 45, "F")
dad = Person("Daddy", 45, "M")
kid1 = Person("Johnie", 2, "M")
kid2 = Person("Janie", 3, "F")
myFamily = Family(mom,dad,kid1,kid2)
kid3 = Person("Paulie", 1, "M")
myFamily.add(kid3)
print(myFamily)

