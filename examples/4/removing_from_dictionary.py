#!/usr/bin/env python3
cars = {'Mustang':'Ford', 'Falcon':'Ford',
        'Camaro':'Chevy', 'Corvette':'Chevy',
        'Eclipse':'Mitsubishi', 'Integra':'Acura'}
unknown = "Make is Unknown"
make = cars.pop("Corvette")
print(make)
make = cars.pop("Accord",unknown)
print(make)
a_tuple = cars.popitem()
print(a_tuple[0], a_tuple[1])
model, make = cars.popitem()
print(model, make)
print(cars)
