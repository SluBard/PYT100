import sys

if len(sys.argv) != 3:
    print("Usage: {} source target".format(sys.argv[0].split('/')[-1]))
    exit()

src = sys.argv[1]
tgt = sys.argv[2]

try:
    s=open(src,"r")
    t=open(tgt,"w")
except OSError as err:
    print(err)
    exit()

while True:
    buff = s.readline()
    if not buff:
        break
    t.write(buff)

s.close()
t.close()
    
