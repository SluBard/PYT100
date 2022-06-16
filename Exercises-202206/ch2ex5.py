#string = input("Enter a string: ")
string = "hello\n"
print("Does string endwith a '.': {}".format( string.endswith(".")))
print("Does string contain all alpha characters: {}".format(string.isalpha()))
print("Does 'x' appear in the string: {}".format("x" in string))
print("How long is the string: {}".format(len(string)))
print("Results of replacing 'e' with 'E': {}".format(string.replace("e","E")))
print("Does '\\n' appear in the string: {}".format("\n" in string))
