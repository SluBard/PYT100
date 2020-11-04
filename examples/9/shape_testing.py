#!/usr/bin/env python3
from shape_circle import Circle
from shape_square import Square
from shape_rectangle import Rectangle

c1 = Circle("Circle1", 10)
s1 = Square("Square1", 5)
r1 = Rectangle("Rectang1e1", 5, 10)

shapes = [ s1, c1, r1 ]
for shape in shapes:
    print("ID", shape.shapeId(), "NAME", 
          shape.myname())
    print("AREA", shape.area())
    print("******************")
