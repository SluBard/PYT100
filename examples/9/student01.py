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
