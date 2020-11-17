import sys, os, time

def printstats01(file,size):
    stat = os.stat(file)
    if os.path.isfile(file) and size<stat.st_size:
        print("File Stats for:", file)
        print("\tsize", ":", stat.st_size)
        print("\tmtime", ":", time.ctime(stat.st_mtime))
        print("\n")
try:
    dirname = sys.argv[1]    
    size = int(sys.argv[2])
except:
    print("Usage: ex4.py dir size")
    exit(1)

try:
    files = os.listdir(dirname)
except:
    print("Not a valid directory name")
    exit(2)

for file in files:
    printstats01(file,size)




    
