from ex1 import Person
class Family(Person):
    def __init__(self,p1,p2,*arg):
        self.p1 = p1
        self.p2 = p2
        self.children = list()
        for c in arg:
            self.children.append(c)
    def add(self,k):
        self.children.append(k)
    def __str__(self):
        s = str(self.p1)+"\n"+str(self.p2)+"\n"
        for k in self.children:
            s += str(k)+"\n"
        return s

if __name__ == "__main__":
    mom=Person("Mommy",45,"F")
    dad=Person("Daddy",45,"M")
    kid1=Person("Johnie",2,"M")
    kid2=Person("Janie",3,"F")
    myFamily=Family(mom,dad,kid1,kid2)
    kid3=Person("Paulie",1,"M")
    myFamily.add(kid3)
    print(myFamily)
        
