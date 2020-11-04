#!/usr/bin/env python3
def usethis(akey):
    return states[akey]

states = {'New Hampshire':'NH', 'Maryland':'MD',
          'Nevada':'NV', 'Maine':'ME'}

long_names = list(states.keys())
long_names.sort(key=usethis)
for name in long_names:
    print(name, states[name])
