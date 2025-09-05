import sys

if len(sys.argv) != 3:
    print("Usage:\npython3 {} inputfile outputfile".format(sys.argv[0]))
    exit()
infile = sys.argv[1]
otfile = sys.argv[2]
i=open(infile,"r")
o=open(otfile,"w")

while True:
    line = i.readline()
    if not line:
        break
    o.write(line)
    line = i.readline()
    
i.close()
o.close()
