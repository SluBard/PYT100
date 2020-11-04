#!/usr/bin/env python3
def add():
    val = input("enter value to add: ")
    lis.append(val)
    
def delete():
    x = lis.pop(0)
    print("removing", x)
    
def display():
    print("displaying:", lis)
    
def terminate():
    print("terminating") 
    exit()
    
lis = []		
themap = {1:add, 2:delete, 3:display, 4:terminate}
while True:
    for index, fun in themap.items():
        print(index, fun.__name__)
    key = int(input("Make selection: "))
    if key in themap.keys():
        themap[key]()
    else:
        print("illegal selection\n")
