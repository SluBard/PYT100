import sys

if len(sys.argv) == 1:
    print("Usage: {} file1 [file2] [...]".format(sys.argv[0].split('/')[-1]))
    exit()

files = sys.argv[1:]

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
    print("{} has Chars: {} Words: {} Lines: {}".format(file,ct,words,lines))    
    f.close()



    
