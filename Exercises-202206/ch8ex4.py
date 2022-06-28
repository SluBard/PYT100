import sys,os, time

if len(sys.argv) != 3:
    print("Usage: {} dir size".format(sys.argv[0].split('/')[-1]))
    exit()

directory = sys.argv[1]
size = sys.argv[2]

files = os.listdir(directory)
fmt="{} bytes:{} mtime:{}"
for file in files:
    info = os.stat(file)
    if info.st_size > int(size):
        print(fmt.format(file,info.st_size,time.ctime(info.st_mtime)))
    
