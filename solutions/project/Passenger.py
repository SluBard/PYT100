#!/usr/bin/env python3
class Passenger:
	""" Passenger Class """

    def __init__(self, fname, lname, flight, seat):
        self.firstname = fname
        self.lastname = lname
        self.flight = flight
        self.seat = seat

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + self.flight + " " + self.seat
