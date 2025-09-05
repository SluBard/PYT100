import sys

if len(sys.argv) == 1:
    print("Usage:\npython {} files...".format(argv[0]))
    exit()

files = sys.argv[1:]

for file in files:
    lines = words = chars = 0
    f=open(file,"r")
    for line in f.readlines():
        lines += 1
        chars += len(line)
        words += len(line.split())
    f.close()
    print("name:{} lines:{} words:{} chars:{}".format(file,lines,words,chars))
