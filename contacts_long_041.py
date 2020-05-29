#!/usr/bin/env python3

import sys

file = sys.argv[1]
a = {}

with open(file) as fd:
    fd = fd.readlines()
    for line in fd:
        line = line[0:-1]
        [left, right] = line.split()
        a[left] = right
for line in sys.stdin:
    try:
        print("Name:", line.strip())
        print("Phone:", a[line.strip()])
    except:
        print("No such contact")
