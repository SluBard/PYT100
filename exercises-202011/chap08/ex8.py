import sys
sys.argv.pop(0)
if sys.argv[0] == '-t':
    totals=1
    sys.argv.pop(0)
else:
    totals=0
tchars = twords = tlines = 0

for fname in sys.argv:
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

    twords += words
    tchars += chars
    tlines += lines
    
    print("Name: {}\tLines: {}\tWords: {}\tChars: {}".format(fname,lines,words,chars))
if totals:
    print("Totals Lines: {}\tWords: {}\tChars: {}".format(tlines,twords,tchars))
