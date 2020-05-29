#!/usr/bin/env python3

from sys import stdin
from sys import argv

lines = stdin.readlines()

with open(argv[1]) as file:
    censored = file.readlines()

    for line in lines:
        line = line.strip()

        for word in censored:
            word = word.strip()
            if word in line.lower():
                line = line.replace(word, ('@' * len(word)))

        print(line)
