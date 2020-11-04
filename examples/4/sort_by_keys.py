#!/usr/bin/env python3
states = {'New Hampshire':'NH', 'Maryland':'MD',
          'Nevada':'NV', 'Maine':'ME'}

long_names = list(states.keys())
print(type(long_names))
long_names.sort()
for name in long_names:
    print(name, states[name])
print()

result = sorted(states)
print(type(result))
for name in result:
    print(name, states[name])
