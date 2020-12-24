from Person import Person

class Family(Person):
    def __init__(self,p1,p2,*kids):
        self.kids = list()
        self.p1 = p1
        self.p2 = p2
        for kid in kids:
            self.kids.append(kid)
    
    def add(self,k):
        self.kids.append(k)

    def __str__(self):
        fam = self.p1.__str__()
        fam += "\n" + self.p2.__str__()
        for kid in self.kids:
            fam += "\n" + kid.__str__()
        return fam
