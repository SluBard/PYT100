s1 = input("Enter a string ")
print("Ends with a '.'? {}".format(s1.endswith(".")))
print("All alpha? {}".format(s1.isalpha()))
print("Contains an 'x'? {}".format('x' in s1))
print("Length of s1? {}".format(len(s1)))
print("Contains '\\n'? {}".format('\n' in s1))
print("'e'->'E' -> {}".format(s1.replace('e','E')))
      
