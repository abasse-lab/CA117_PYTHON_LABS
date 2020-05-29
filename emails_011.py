#!/usr/bin/env python3

import sys

d = '0123456789'
s = '@'
for line in sys.stdin:
    first, last = line.split(s)
    first = first.strip(d).title().split('.')
    print(' '.join(first))
