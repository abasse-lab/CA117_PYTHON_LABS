#!/usr/bin/env python3

import sys

def capitalize(s):
    return s[0].capitalize() + s[1:-1] + s[-1].capitalize()

def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        if len(line) > 1:
            capital = capitalize(line)
            print(capital)


if __name__ == '__main__':
    main()
