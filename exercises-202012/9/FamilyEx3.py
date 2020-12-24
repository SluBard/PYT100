from Person import Person
from FamilyError import FamilyError

class Family(Person):
    def __init__(self,p1,p2,*kids):
        self.kids = list()
        if isinstance(p1,Person):
            self.p1 = p1
        else:
            raise FamilyError("Not a Person Object")
        if isinstance(p2,Person):
            self.p2 = p2
        else:
            raise FamilyError("Not a Person Object")
        for kid in kids:
            if isinstance(kid,Person):
                self.kids.append(kid)
            else:
                raise FamilyError("Not a Person Object")
            
    
    def add(self,kid):
        if isinstance(kid,Person):
            self.kids.append(kid)
        else:
            raise FamilyError("Not a Person Object")

    def __str__(self):
        fam = ""
        fam += self.p1.__str__()
        fam += "\n" + self.p2.__str__()
        for kid in self.kids:
            fam += "\n" + kid.__str__()
        return fam
