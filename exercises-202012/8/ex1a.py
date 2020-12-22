infile = input("Enter input filename: ")
outfile = input("Enter output filename: ")
fin=open(infile,"r")
fout=open(outfile,"w")
while True:
    line=fin.readline()
    if not line:
        break
    fout.write(line)
fin.close()
fout.close()
