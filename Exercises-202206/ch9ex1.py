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

p1 = Person("Michael",45,"M")
print(p1)
