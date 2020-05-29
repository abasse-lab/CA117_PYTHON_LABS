#!/usr/bin/env python3

import sys
i = 0
for line in sys.stdin:
  while i < len(line):
    line = line.strip().title()
    i += 1
  print(line)
