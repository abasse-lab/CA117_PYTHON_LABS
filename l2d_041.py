#!/usr/bin/env python3

import sys

def l2d(c):
   l = []
   b = {}
   for lines in c:
      l.append(lines.strip().split())
   i = 0
   while i < len(l[1]):
      b[l[0][i]] = l[1][i]
      i = i + 1
   return b

if __name__ == '__main__':
    main()
