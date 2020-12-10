s1 = input("Enter data: ")

print("Does input end in a period? {}".format(s1.endswith('.')))
print("Does input contain all alpha? {}".format(s1.isalpha()))
print("Is there an 'x' in the string? {}".format('x' in s1))
print("Length of string is: {}".format(len(s1)))
print("Change 'e' to 'E'\nOriginal: {}\nModified: {}".format(s1,s1.replace('e','E')))
