src = input("Enter the name of the input file: ")
tgt = input("Enter the name of the output file: ")

s=open(src,"r")
t=open(tgt,"w")

while True:
    buff = s.readline()
    if not buff:
        break
    t.write(buff)

s.close()
t.close()
    
