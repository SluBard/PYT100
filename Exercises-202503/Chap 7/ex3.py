total = 0
while True:
    try:
        data = input("enter integer (end to exit)")
        if data == "end":
            break
  
        total += int(data)
        
    except ValueError:
        print("Please enter only integers.")
    except KeyboardInterrupt:
        print("\nPlease enter 'end' to exit.")
    except EOFError:
        print()
        break

print("Total of integers entered is: {}".format(total))
