#!/usr/bin/env python3

import sys

v = 'aeiou'

for line in sys.stdin:
    line = line.strip()
    words = ''
    i = 0
    while i < len(line):
        words += line[i]
        if line[i] in v:
        	i += 2

        i += 1

    print(words)
