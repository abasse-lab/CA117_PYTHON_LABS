#!/usr/bin/env python3

import sys
args = int(sys.argv[1])
i = 1

c = args + 1
while i < c - 1:
  line = (c - i - 1) * " " + "* " * i
  print(line[:len(line) - 1])
  i += 1
i = 0
while i < c - 1:
  line = i * " " + "* " * (c - i - 1)
  print(line[:len(line) - 1])
  i += 1
