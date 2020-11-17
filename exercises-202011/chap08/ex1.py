
inp = input("Enter input filename: ")
out = input("Enter output filename: ")

inpf = open(inp,'r')
outf = open(out,'w')

while True:
    data = inpf.readline()
    if not data:
        break
    outf.write(data)

inpf.close()
outf.close()
    
