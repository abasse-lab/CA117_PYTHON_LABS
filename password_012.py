#!/usr/bin/env python

import sys

def passw(s):
    a = 0
    b = 0
    c = 0
    d = 0
    for element in s:
        if element.isdigit():
            a = 1
        elif element.isupper():
            b = 1
        elif element.islower():
            c = 1
        else:
            d = 1
    return a + b + c + d

def main():
    for line in sys.stdin:
        print(passw(line.strip()))

if __name__ == '__main__':
    main()
