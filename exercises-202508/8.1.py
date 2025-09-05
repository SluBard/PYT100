infile = input("Input file: ")
otfile = input("Output file: ")
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
