#!/usr/bin/env python3
txt = "| "
for character in "Hello":
    txt += character + " | "
print(txt)

txt = "range(5): "
for i in range(5):   # (b,e]  0,1,2,3,4
   txt += str(i) + " "
print(txt)

txt = "range(5, 10): "
for i in range(5, 10): # (5,10] 5,6,7,8,9
   txt += str(i) + " "
print(txt)

txt = "range(1, 20, 2): "
for i in range(1, 20, 2):# (1,20] 1 3 5 7 9 11 13 15 17 19
   txt += str(i) + " "
print(txt)
