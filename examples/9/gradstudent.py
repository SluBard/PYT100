#!/usr/bin/env python3
from student02 import Student
class GradStudent(Student):
    """ GradStudent Class """
    
    def  __init__(self, name, major, stipend):
        Student.__init__(self, name, major)
        self.stipend = stipend
        
    def getstipend(self):
        return self.stipend
    
    def setstipend(self, stipend):
        self.stipend = stipend
        
    def __str__(self):
        parent = Student.__str__(self)
        return parent + " " + str(self.stipend)
        #return Student.__str__(self) + " " + str(self.stipend)
