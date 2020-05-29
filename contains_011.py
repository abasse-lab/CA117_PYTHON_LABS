#!/usr/bin/env python

import sys

''' soooooooooo like substring you want to see if elements on
the left hand side is contained exasctly on the right hand side. '''

for line in sys.stdin:
  [left, right] = line.upper().strip().split()
  i = 0
  count = 0
  while i < len(left):
    j = 0
    if left[i] in right:
      count = count + 1
      right = right.replace(left[i], ' ', 1)
    i += 1
  if count == len(left):
    print(True)
  else:
    print(False)
