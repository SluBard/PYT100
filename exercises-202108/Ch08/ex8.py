import sys

if len(sys.argv) <= 1:
    print("Usage:",sys.argv[0].split('\\')[-1],"file1 ... filen")
    exit(0)
    
want_totals = 0
if sys.argv[1] == "-t":
    want_totals = 1
    sys.argv.pop(0)
    
total_lines = total_words = total_chars = 0

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
    total_lines += lines
    total_words += words
    total_chars += chars

if want_totals:
    print("\nTotals\n\tlines = {}\twords = {}\tchars = {}".format(total_lines,total_words,total_chars))
