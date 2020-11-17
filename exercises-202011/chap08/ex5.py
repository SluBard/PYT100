import sys

fn1 = sys.argv[1]
fn2 = sys.argv[2]

f1 = open(fn1,'r')
f2 = open(fn2,'r')

s1 = set()
for i in f1:
    s1.add(i.strip())

s2 = set()
for i in f2:
    s2.add(i.strip())

print(list(s1 & s2))
