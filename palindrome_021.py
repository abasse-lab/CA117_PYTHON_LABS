#!/usr/bin/env python3

import sys

for line in sys.stdin:
    p = []
    line = line.strip().lower()

    for c in line:
        if c.isalnum():
            p.append(c)

    if p == p[::-1]:
        print(True)
    else:
        print(False)
