import sys
chars = words = lines = 0
file = open(sys.argv[1], "r")

while True:
    line = file.readline()
    if not line:
        break
    words += len(line.split())
    chars += len(line)
    lines += 1
    
file.close()
print("Lines: {}\tWords: {}\tChars: {}".format(lines,words,chars))
