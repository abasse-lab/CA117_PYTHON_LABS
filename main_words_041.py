#!/usr/bin/env python3

import sys

a =[]
for line in sys.stdin:
    line = line.strip().split()
    a.append(line)

uniq = []
every = []
count = []

for line in a:
    for x in line:
        every.append(x.lower())
        if len(x.lower()) > 3:
            if x.lower() not in uniq:
                uniq.append(x.lower)
                print(x)