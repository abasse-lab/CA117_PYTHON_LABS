#!/usr/bin/env python3

import sys

for line in sys.stdin:
  [left, right] = line.strip().split()

  list_str1 = list(left)
  list_str1.sort()
  list_str2 = list(right)
  list_str2.sort()

  if list_str1 == list_str2:
    print(True)

  else:
    print(False)
