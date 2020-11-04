#!/usr/bin/env python3
txt = "| "
for character in "Hello":
    txt += character + " | "
print(txt)

txt = "range(5): "
for i in range(5):
   txt += str(i) + " "
print(txt)

txt = "range(5, 10): "
for i in range(5, 10):
   txt += str(i) + " "
print(txt)

txt = "range(1, 20, 2): "
for i in range(1, 20, 2):
   txt += str(i) + " "
print(txt)
