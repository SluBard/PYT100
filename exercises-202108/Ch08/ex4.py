import sys,os,time

try:
    directory = sys.argv[1]
    size = sys.argv[2]
except:
    print("Usage:",sys.argv[0].split('\\')[-1],"directory_name size")
    exit(0)
    
files = os.listdir(directory)

for file in files:
    info = os.stat(file)
    if info.st_size > int(size):
        print("{:15} {:5} {:>30}".format(file,info.st_size,time.ctime(info.st_mtime)))
