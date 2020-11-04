#!/usr/bin/env python3
names = ['Mike', 'John',  'Jane',  'Alice']
themap = {'Mike':15, 'Chris':10, 'Dave':25}

while True:
    try:
        value = input("\n\nEnter an integer: ")
        if value == "end":
            break

        value = int(value)
        print("Name is: " + names[value])
        name = input("Enter a name: ")
        print(name, " => ", themap[name])

    except ValueError:
        print("Value Error: non numeric data")

    except IndexError as ie:
        print("Illegal subscript:", ie)

    except KeyError as ke:
        print("Illegal key")

    except:
        print("Unknown Error: ")
