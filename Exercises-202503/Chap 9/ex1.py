class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_gender(self,gender):
        self.gender=gender
        
    def __str__(self):
        return self.name + " " + str(self.age) + " " +self.gender

p1 = Person("Michael",45,"M")
print(p1)
