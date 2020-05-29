#!/usr/bin/env python3

import sys

arg = sys.argv[1]
mapping = {}
with open(arg) as f:
    maps = f.readlines()
for i in maps:
    i = i.strip().split()
    mapping[i[0]] = i[1]

num = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten'
}

text = sys.stdin.readlines()
for line in text:
    a = []
    line = line.split()
    i = 0
    while i < len(line):
        if line[i] in num:
            a.append(mapping[num[line[i]]])
        else:
            a.append('unknown')
        i += 1
    a = " ".join(a)
    print(a)
