
class Passenger:
    def __init__(self,first,last,flight_number,seat_number):
        self.first = first
        self.last = last
        self.flight_number = flight_number
        self.seat_number = seat_number
    def getfirst(self):
        return self.first
    def getlast(self):
        return self.last
    def getflightnumber(self):
        return self.flight_number
    def getseatnumber(self):
        return self.seat_number
        
class Passengers:
    def __init__(self,flights):
        f = open("passengers.txt","r")
        for line in f:
            line = line.strip()
            passenger = Passenger(*line.split(","))
            flight = flights.getflight(passenger.getflightnumber())
            flight.addpassenger(passenger)
        f.close()
