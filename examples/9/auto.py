#!/usr/bin/env python3
class Auto:
    """This is the Auto class file"""
    howmany = 0 
    def __init__(self, make, model):
        self.make = make
        self.model = model
        Auto.howmany += 1
    def __del__(self):
        Auto.howmany -= 1
        print("deleting: " + self.make)
        print("count is now:", Auto.howmany)
    def count(self):
        return Auto.howmany
