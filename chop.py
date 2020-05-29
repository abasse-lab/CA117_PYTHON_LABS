#!/usr/bin/env python

'''REMOVE FIRST AND LAST CHARACTER FROM A STRING'''

import sys

def chop(s):
  s[1:len(s) - 1]

def main():
  for line in sys.stdin:
    chopped = chop(line.strip())
    if len(chopped) > 0:
      print(chopped)

