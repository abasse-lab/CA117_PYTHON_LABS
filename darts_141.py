#!/usr/bin/env python3
import sys
from math import sqrt

total = []
for line in sys.stdin:
    x, y = line.strip().split()
    d = sqrt(int(x) ** 2 + int(y) ** 2)
    pts = 11 - (d / 20)

    if pts > 10:
        total.append(10)
    else:
        total.append(int(pts))

print(sum(total))
