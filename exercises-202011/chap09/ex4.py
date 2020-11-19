from ex1 import Person
class FamilyError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class Family(Person):
    def __init__(self,p1,p2,*arg):
        try:
            if not isinstance(p1,Person):
                raise FamilyError("First Parent not a Person")
            if not isinstance(p2,Person):
                raise FamilyError("Second Parent not a Person")
            for c in arg:
                if not isinstance(c,Person):
                    raise FamilyError("Child not a Person")
        except FamilyError as err:
            print(err)
            
        self.p1 = p1
        self.p2 = p2
        self.children = list()
        for c in arg:
            self.children.append(c)
            
    def add(self,k):
        try:
            if not isinstance(k,Person):
                raise FamilyError("Child not a Person")
        except FamilyError as err:
            print(err)
        self.children.append(k)
        
    def __str__(self):
        s = str(self.p1)+"\n"+str(self.p2)+"\n"
        for k in self.children:
            s += str(k)+"\n"
        return s
    
    def __gt__(self,other):
        return len(self.children) > len(other.children)

    def __lt__(self,other):
        return len(self.children) < len(other.children)

    def __eq__(self,other):
        return len(self.children) == len(other.children)
if __name__ == "__main__":
    mom=Person("Mommy",45,"F")
    dad=Person("Daddy",45,"M")
    kid1=Person("Johnie",2,"M")
    kid2=Person("Janie",3,"F")
    kid3=Person("Paulie",1,"M")

    myFamily = Family(mom, dad, kid1, kid2)
    smiths = Family(mom, dad, kid1)
    if (myFamily > smiths):
        print("we have more kids than smiths")
    if (myFamily == smiths):
        print("families have same # of kids")
    if (myFamily < smiths):
        print("we have fewer kids than smiths")
        
