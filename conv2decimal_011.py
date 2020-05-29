#!/usr/bin/env python3

import sys

def conv(left, right):
  left = left[::-1]
  dec = 0
  i = 0
  while i < len(left):
    dec = dec + int(left[i]) * int(right) ** i
    i += 1
  return dec

def main():
  for line in sys.stdin:
    [num, base] = line.strip().split()
    print(conv(num, base))

if __name__ == '__main__':
  main()
