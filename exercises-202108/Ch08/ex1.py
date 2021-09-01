ifile = input("Enter input file name: ")
ofile = input("Enter output file name: ")

inf = open(ifile,"r")
ouf = open(ofile,"w")

line = inf.readline()
while line:
    ouf.write(line)
    line = inf.readline()

inf.close()
ouf.close()
