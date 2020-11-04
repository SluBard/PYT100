#!/usr/bin/env python3
import pickle
values = [50, 32.29, "Michael"]
f = open("output", "wb")
for value in values:
    pickle.dump(value, f)
f.close()
