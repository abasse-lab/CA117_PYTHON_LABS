#!/usr/bin/env python

import sys

def sumfac(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n / i
        i += 1

    return (True if sum == n and n != 1 else False)

def main():
    for line in sys.stdin:
        line = int(line)
        print(sumfac(line))


if __name__ == '__main__':
    main()
