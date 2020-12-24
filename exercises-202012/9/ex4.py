from Person import Person
from FamilyEx4 import Family
from FamilyError import FamilyError

mom = Person("Mommy", 45, "F")
dad = Person("Daddy", 45, "M")
kid1 = Person("Johnie", 2, "M")
kid2 = Person("Janie", 3, "F")
myFamily = Family(mom, dad, kid1, kid2)
smiths = Family(mom,dad,kid1)
if myFamily > smiths:
    print("We have more kids than the smiths")
if myFamily == smiths:
    print("We have the same # of kids")
if myFamily < smiths:
    print("We have fewer kids than the smiths")


