import sys

sys.argv.pop(0)

for fname in sys.argv:

    file = open(fname, "r")
    chars = words = lines = 0

    while True:
        line = file.readline()
        if not line:
            break
        words += len(line.split())
        chars += len(line)
        lines += 1
    
    file.close()
    print("Name: {}\tLines: {}\tWords: {}\tChars: {}".format(fname,lines,words,chars))
