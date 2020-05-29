#!/usr/bin/env python3


import sys

b = []
c = []
for line in sys.stdin:
    b.append(line.strip())
    avg = sum(len(x) for x in b) / len(b)

for x in b:
    if len(x) > avg:
        c.append(x)
        x = '\n'.join(c)

print('Average: {:.2f}'.format(avg) + '\n' + x)
