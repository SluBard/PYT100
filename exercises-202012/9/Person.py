class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender
    def name(self):
        return self.name
    def age(self):
        return self.age
    def gender(self):
        return self.gender
    def setname(self,name):
        self.name = name
    def setage(self,age):
        self.age = age
    def setgender(self,gender):
        self.gender = gender
    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.gender
