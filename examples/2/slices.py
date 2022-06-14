#!/usr/bin/env python3
text = "Spam and eggs"

s1 = text[0]               # "S"
s2 = text[5:8]             # "and"        (b,e]
s3 = text[4:]              # " and eggs"
s4 = text[:4]              # "Spam"
s5 = text[-1]              # "s"
s6 = text[-3:-1]           # "gg"

fmt = "{0}|{1}|{2}|{3}|{4}|{5}"
print(fmt.format(s1, s2, s3, s4, s5, s6))
