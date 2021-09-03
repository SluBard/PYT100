class FamilyError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def get_msg(self):
        return self.msg
    
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
            try:
                if isinstance(kid,Person):
                    self.kids.append(kid)
                else:
                    raise FamilyError("Error: can only add Person Class")
            except FamilyError as e:
                print(e.get_msg())
    def add(self,kid):
        try:
            if isinstance(kid,Person):
                self.kids.append(kid)
            else:
                raise FamilyError("Error: can only add Person Class")
        except FamilyError as e:
            print(e.get_msg())
        
    def __str__(self):
        buf = str(self.p1)+"\n"+str(self.p2)
        for kid in self.kids:
            buf += "\n\t"+str(kid)
        return buf
    def __eq__(self,rhs):
        return len(self.kids) == len(rhs.kids)
    def __gt__(self,rhs):
        return len(self.kids) > len(rhs.kids)
    def __lt__(self,rhs):
        return len(self.kids) < len(rhs.kids)    

    
p1 = Person("Mommy",45,"F")
p2 = Person("Daddy",45,"M")
k1 = Person("Johnny",2,"M")
k2 = Person("Janie",3,"F")

family = Family(p1,p2,k1,k2)
smiths = Family(p1,p2,k1)

if family > smiths: #family.__eq__(smiths)
    print("We have more kids than the smiths")
if family == smiths:
    print("We have the same number of kids as the smiths")
if family < smiths:
    print("We have less kids than the smiths")
          

