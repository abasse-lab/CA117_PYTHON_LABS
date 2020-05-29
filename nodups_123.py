#!/usr/bin/env python3

import sys
import string


a = []
for line in sys.stdin:
    b = []
    for x in line.split():
        if x.lower().strip(string.punctuation) not in a:
            a.append(x.lower().strip(string.punctuation))
            b.append(x)
        else:
            b.append('.')
    print(' '.join(b))
