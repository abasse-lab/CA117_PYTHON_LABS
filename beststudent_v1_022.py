#!/usr/bin/env python3

import sys

token = sys.argv[1]

with open(token) as fd:
    c = [0]
    v = ['']
    fd = fd.readlines()
    for line in fd:
        line = line.strip()
        e = line[0:2]
        if int(e) > int(c[0]):
            c.pop(0)
            c.append(e)
            v.pop(0)
            v.append(line[3:])
    print('Best student:', v[0])
    print('Best mark:', c[0])
