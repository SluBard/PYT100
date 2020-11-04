#!/usr/bin/env python3
class Flight:
	""" Flight Class """

    def __init__(self, fromm, to, number):
        self.number = number
        self.fromm = fromm
        self.to = to
        self.people = []
	
    def __str__(self):
        return self.fromm + " " + self.to + " " + self.number

    def listing(self):
        print("FLIGHT", self.number)
        num = 1
        for i in self.people:
            print(num, i)
            num += 1
        print("END OF FLIGHT", self.number)

    def flightno(self):
        return self.number

    def add(self, p):
        self.people.append(p)

    def howmany(self):
        return len(self.people)
