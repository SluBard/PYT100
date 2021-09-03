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

class Family:
    def __init__(self,p1,p2,*kids):
        self.p1=p1
        self.p2=p2
        self.kids=list()
        for kid in kids:
            self.kids.append(kid)
    def add(self,kid):
        self.kids.append(kid)
    def __str__(self):
        buf = str(self.p1)+"\n"+str(self.p2)
        for kid in self.kids:
            buf += "\n\t"+str(kid)
        return buf

p1 = Person("Mommy",45,"F")
p2 = Person("Daddy",45,"M")
k1 = Person("Johnny",2,"M")
k2 = Person("Janie",3,"F")
family = Family(p1,p2,k1,k2)
k3 = Person("Paulie",1,"M")
family.add(k3)
print(family)

