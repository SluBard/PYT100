total=0
while True:
    input1 = input("Enter a number: ")

    try:
        total += int(input1)
            
    except ValueError:
        print("Please enter integers only.")
        
    except KeyboardInterrupt:
        print("Ctl-C pressed.")

    except EOFError:
        break

print("Total of all values entered is {}".format(total))
        
    
