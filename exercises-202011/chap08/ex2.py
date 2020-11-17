import sys
inp = sys.argv[1]
out = sys.argv[2]

inpf = open(inp,'r')
outf = open(out,'w')

while True:
    data = inpf.readline()
    if not data:
        break
    outf.write(data)

inpf.close()
outf.close()
    
