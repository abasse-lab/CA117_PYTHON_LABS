#!/usr/bin/env python3
import sys

def main():
  lines = sys.stdin.readlines()
  maxlen = 0
  for item in lines:
    a = item.strip().split()
    club = " ".join(a[1:len(a) - 8])
    if len(club) > maxlen:
      maxlen = len(club)
  print("{:^4s}{:<{}.{}s}{:>3s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}".format("POS", "CLUB", maxlen, maxlen, "P", "W", "D", "L", "GF", "GA", "GD", "PTS"))
  for line in lines:
    a = line.strip().split()
    club = " ".join(a[1:len(a) - 8])
    print("{:>3s}{:<{}.{}s}{:>3s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}".format(a[0], " " + club, maxlen + 1, maxlen + 1, a[len(a) - 8], a[len(a) - 7], a[len(a) - 6], a[len(a) - 5], a[len(a) - 4], a[len(a) - 3], a[len(a) - 2], a[len(a) - 1]))

if __name__ == '__main__':
  main()
