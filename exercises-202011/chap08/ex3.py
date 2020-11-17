import sys
inp = sys.argv[1]
out = sys.argv[2]

try:
    inpf = open(inp,'r')
    outf = open(out,'w')
except OSError as err:
    print(err)
    exit(1)
    
while True:
    data = inpf.readline()
    if not data:
        break
    outf.write(data)

inpf.close()
outf.close()
    
