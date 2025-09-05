import sys

if len(sys.argv) == 1:
    print("Usage:\npython {} files...".format(argv[0]))
    exit()


totals=False
tlines = twords = tchars = 0
sys.argv.pop(0)
if sys.argv[0] == "-t":
    totals = True
    sys.argv.pop(0)
    
files = sys.argv

for file in files:
    lines = words = chars = 0
    f=open(file,"r")
    for line in f.readlines():
        lines += 1
        words += len(line.split())
        chars += len(line)
    f.close()
    print("name:{} lines:{} words:{} chars:{}".format(file,lines,words,chars))
    tlines += lines
    twords += words
    tchars += chars

if totals:
    print("Totals\n\tlines:{} words:{} chars:{}".format(tlines,twords,tchars))

        
