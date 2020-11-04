#!/usr/bin/env python3
class Employee:
    pass
class Manager(Employee):
    pass
class Executive(Manager):
    pass

m = Manager()

print(isinstance(m, Employee))            #True
print(isinstance(m, Manager))             #True
print(isinstance(m, Executive))           #False

print(issubclass(Executive, Executive))   #True
print(issubclass(Executive, Manager))     #True
print(issubclass(Executive, Employee))    #True
print(issubclass(Executive, object))      #True
