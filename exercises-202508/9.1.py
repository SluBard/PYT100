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

p1=Person("Michael",45,"M")
p1.setname("Mike")
p1.setage(44)
print(p1)

