import os,sys, time

if len(sys.argv) !=3:
    print("Usage: {} dir size".format(sys.argv[0]))
    exit(1)

dirname=sys.argv[1]
size=int(sys.argv[2])


if not os.path.isdir(dirname):
    print("{} not the name of a directory".format(dirname))
    exit(1)

dirlist = os.listdir(dirname)
os.chdir(dirname)
for file in dirlist:
    #print(file)
    fstat=os.stat(file)
    if fstat.st_size > size:
        print("{}\t{}\t{}".format(file,fstat.st_size,time.ctime(fstat.st_mtime)))
        

