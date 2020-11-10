numbers = { '0':'zero','1':'one','2':'two','3':'three','4':'four',
            '5':'five','6':'six','7':'seven','8':'eight','9':'nine' }
while True:
    data = input("enter a number (q to quit): ")
    if data == 'q':
        break
    for number in data:
        print(numbers.get(number),end=' ')
    print()
