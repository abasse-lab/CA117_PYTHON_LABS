#!/usr/bin/env python3

import sys

for line in sys.stdin:
    a = line.strip()
    a = ''
    for word in line.split():
        a += word[:-1] + word[-1].upper() + ' '
    print(a[:-1])
