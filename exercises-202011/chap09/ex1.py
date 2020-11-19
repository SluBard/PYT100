class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.gender

if __name__ == "__main__":
    p1 = Person("Micahel",45,"M")
    print(p1)
