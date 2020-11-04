#!/usr/bin/env python3
class Student:
    """ This is the Student class file """
    
    def __init__(self, name, major):
        self.thename = name
        self.themajor = major

    def major(self):
        return self.themajor
    def name(self):
        return self.thename

    def setname(self, newname):
        self.thename  = newname
    def setmajor(self, newmajor):
        self.themajor = newmajor

    def __del__(self):
        print("Debug: Deleting " + self.thename)

    def __len__(self):
        length = 4 # default degree length
        if self.themajor == "Accounting":
            length = 2 # 2 year degree
        return length

    def __str__(self):
        return self.thename + " " + self.themajor
