#!/usr/bin/env python3

import sys
d = {}
v = ['a', 'e', 'i', 'o', 'u']

for line in sys.stdin:
    line = line.strip()
    i = 0
    n = 0
    while i < len(line):
        try:
            if line[i] == line[i + 1] and line[i] in v:
                n += 1
        except:
            pass
        i += 1
    d[line] = n

print(max(d, key=d.get))
