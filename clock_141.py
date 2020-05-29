#!/usr/bin/env python3

import sys

l = []
for line in sys.stdin:
    l.append(line.strip())

a = int(l[0])
b = int(l[1])

v = [b - a, (b - 12) - a, (b + 12) - a]
m = min(v, key=abs)
if m == -6:
    m = 6
print(m)
