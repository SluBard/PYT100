import sys

try:
    ifile = sys.argv[1]
    ofile = sys.argv[2]
except:
    print("Usage:",sys.argv[0].split('\\')[-1],"input_file output_file")
    exit(0)

inf = open(ifile,"r")
ouf = open(ofile,"w")

line = inf.readline()
while line:
    ouf.write(line)
    line = inf.readline()

inf.close()
ouf.close()
