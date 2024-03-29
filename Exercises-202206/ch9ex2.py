class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return "{} {} {}".format(self.name,self.age,self.gender)

    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name
    def setage(self,age):
        self.age = age
    def getage(self):
        return self.age
    def setgender(self,gender):
        self.gender = gender
    def getgender(self):
        return self.gender

class Family:
    def __init__(self,p1,p2,*k):
        self.p1 = p1
        self.p2 = p2
        self.kids = list()
        for i in k:
            self.kids.append(i)
    def __str__(self):
        string = "{}\n{}".format(self.p1,self.p2)
        for kid in self.kids:
            string += "\n\t{}".format(kid)
        return string
    def add(self,k):
        self.kids.append(k)

p1 = Person("Mom",45,"F")
p2 = Person("Dad",45,"M")
k1 = Person("Johnie",2,"M")
k2 = Person("Janie",3,"F")
family = Family(p1,p2,k1,k2)

k3 = Person("Paulie",1,"M")
family.add(k3)
print(family)
