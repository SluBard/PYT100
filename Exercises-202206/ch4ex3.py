dict1 = { '0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five',
          '6':'six','7':'seven','8':'eight','9':'nine' }

while True:
    input1 = input("Enter a number (q to quit): ")
    if input1 == 'q':
        break
    for digit in input1:
        print("{} ".format(dict1.get(digit)),end="")
    print()
