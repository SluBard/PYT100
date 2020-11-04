#!/usr/bin/env python3
from shape import Shape

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
        
    def __str__(self):
        return "Rectangle: " + self.name + \
               " Length:" + str(self.length) + \
               " Width:" + str(self.width)
    
    def area(self):
        return self.length * self.width
