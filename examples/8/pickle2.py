#!/usr/bin/env python3
import pickle

f = open("output", "rb")
value = pickle.load(f)
cost = pickle.load(f)
name = pickle.load(f)
f.close()

print(name, cost, value)
