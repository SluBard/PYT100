#!/usr/bin/env python3

from Passenger import Passenger
from Flight import Flight

flights = [ ]
#
#	read flight info
#
print ("*** Listing flight information ***");
ffile = open("flights.txt", "r")
for i in ffile:
    (ffrom, to, number) = i.split(",")
    number = number.strip()
    flights.append(Flight(ffrom, to, number))
	
print("There are %s flight records in all \n" % len(flights))
print("*** Now listing flights ***")
for i in flights:
    print(i)
	
print("\n*** opening passenger file ***")	
pfile = open("passengers.txt", "r")
print("*** processing passengers  ***")
for i in pfile:
    (fname, lname, flight, seat) = i.split(",")
    seat = seat.strip()
    print("processing", fname, lname)
    for f in flights:
        if(f.flightno() == flight):
            f.add(Passenger(fname, lname, flight, seat))
            break;
		
print("\n\n*** Printing flight logs now ***")
for i in flights:
    print("\nTHIS FLIGHT HAS", i.howmany(), "PASSENGERS")
    i.listing()
