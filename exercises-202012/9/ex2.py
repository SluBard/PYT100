from Person import Person
from Family import Family

mom = Person("Mommy", 45, "F")
dad = Person("Daddy", 45, "M")
kid1 = Person("Johnie", 2, "M")
kid2 = Person("Janie", 3, "F")
myFamily = Family(mom, dad, kid1, kid2)
kid3 = Person("Paulie", 1, "M")
myFamily.add(kid3)
print(myFamily)
