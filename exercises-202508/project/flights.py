
class Flight:
    def __init__(self,departure,destination,flight_number):
        self.departure = departure
        self.destination = destination
        self.flight_number = flight_number
        self.manifest = list()
    def getdeparture(self):
        return self.departure
    def getdestination(self):
        return self.destination
    def getflightnumber(self):
        return self.flight_number
    def addpassenger(self,passenger):
        self.manifest.append(passenger)
    def getmanifest(self):
        return self.manifest
    def getpassengercount(self):
        return len(self.manifest)
    def __str__(self):
        string = "{} -> {} ({}) has {} passengers\n".format(self.departure,self.destination,self.flight_number,self.getpassengercount())
        for passenger in self.getmanifest():
            string +="\t{}, {} - seat {}\n".format(passenger.getlast(),passenger.getfirst(),passenger.getseatnumber())
        return string

class Flights:
    def __init__(self):
        self.flights = list()
        f = open("flights.txt","r")
        for flight in f:
            flight=flight.strip()
            self.flights.append(Flight(*flight.split(",")))
        f.close()
    def getflights(self):
        return self.flights
    def getflight(self,flightnumber):
        for flight in self.flights:
            if flightnumber == flight.getflightnumber():
                return flight
    def __str__(self):
        string=""
        for flight in self.getflights():
            string += str(flight)
        return string
