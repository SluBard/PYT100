#!/usr/bin/env python3
class Shape:
    idnumber = 100
    def __init__(self, name):
        self.name = name
        self.number = Shape.idnumber
        Shape.idnumber += 1
        
    def shapeId(self): 
        return self.number
    
    def myname(self): 
        return self.name
    
    def area(self): 
        pass
