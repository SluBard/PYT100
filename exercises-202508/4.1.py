myset=set()
notadded=0
while True:
    text = input("Enter a number (end to quit): ")
    if text.lower() == "end":
        break;
    number = int(text)
    if number in myset:
        notadded += 1
    else:
        myset.add(number)
print("myset = {}".format(myset))
print("number of items not added: {}".format(notadded))
