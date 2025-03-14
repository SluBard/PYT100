import sys

if len(sys.argv) !=3:
    print("Usage: {} infile outfile".format(sys.argv[0]))
    exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]
try:
    fin=open(infile,"r")
    fout=open(outfile,"w")
except OSError as err:
    print(err)
    exit(1)
    
while True:
    line=fin.readline()
    if not line:
        break
    fout.write(line)
fin.close()
fout.close()

