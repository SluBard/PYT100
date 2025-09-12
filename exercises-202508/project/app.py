from flights import Flights
from passengers import Passengers

def main():
    flights = Flights()
    passengers = Passengers(flights)
    print(flights)

if __name__ == "__main__":
    main()

