#!/usr/bin/env python

import sys

def plural():
  vowels = 'aeiou'
  for line in sys.stdin:
    line = line.strip()
    if line[-2:] == "ch" or line[-2:] == 'sh' or line[-1] == 'x' or line[-1] == 's' or line[-1] == 'z':
      print(line + 'es')
    elif line[-2] not in vowels and line[-1] == 'y':
      print(line[:-1] + 'ies')
    elif line[-2:] == "fe":
      print(line[:-2] + "ves")
    elif line[-1] == "f":
      print(line[:-1] + "ves")
    elif line[-1] in vowels:
      print(line + "es")
    else:
      print(line + "s")

if __name__ == '__main__':
  plural()
