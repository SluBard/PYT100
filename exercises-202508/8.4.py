import sys, os, time

if len(sys.argv) != 3:
    print("Usage:\npython3 {} directory min_size".format(sys.argv[0]))
    exit()

wdir = sys.argv[1]
size = int(sys.argv[2])

if not os.path.isdir(wdir):
    print("{} is not a directory".format(wdir))
    exit()


os.chdir(wdir)
files = os.listdir(wdir)
for file in files:
    if os.path.isfile(file):
        stat=os.stat(file)
        if stat.st_size > size:
            print("{:<20} {:>10} {:>30}".format(file,stat.st_size,time.ctime(stat.st_mtime)))
