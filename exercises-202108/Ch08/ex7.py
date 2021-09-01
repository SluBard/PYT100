import sys

if len(sys.argv) <= 1:
    print("Usage:",sys.argv[0].split('\\')[-1],"file1 ... filen")
    exit(0)

for file in sys.argv[1:]:
    tfile = open(file,"r")
    lines = words = chars = 0
    tlines = tfile.readlines()
    lines += len(tlines)
    for line in tlines:
        words += len(line.split())
        chars += len(line)
    tfile.close()
    print("{}\tlines = {}\twords = {}\tchars = {}".format(file,lines,words,chars))
