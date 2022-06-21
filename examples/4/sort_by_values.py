#!/usr/bin/env python3
def usethis(akey):
    return states[akey]

states = {'New Hampshire':'NH', 'Maryland':'MD',
          'Nevada':'NV', 'Maine':'ME'}

long_names = list(states.keys())
print(long_names)
long_names.sort(key=usethis)
print(long_names)
for name in long_names:
    print(name, states[name])
