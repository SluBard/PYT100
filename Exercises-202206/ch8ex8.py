import sys

if len(sys.argv) == 1:
    print("Usage: {} [-t] file1 [file2] [...]".format(sys.argv[0].split('/')[-1]))
    exit()

totals = False
tc = tw = tl = 0

files = sys.argv[1:]

if files[0] == "-t":
    totals = True
    files = sys.argv[2:]

for file in files:
    f = open(file, "r")
    ct = words = lines = 0

    while True:
        line = f.readline()
        if not line:
            break
        ct += len(line)
        words += len(line.split())
        lines += 1
    f.close()
    print("{} has Chars: {} Words: {} Lines: {}".format(file,ct,words,lines))
    tc += ct
    tw += words
    tl += lines

if totals == True:
        print("Totals - Chars: {} Words: {} Lines: {}".format(tc,tw,tl))


    
