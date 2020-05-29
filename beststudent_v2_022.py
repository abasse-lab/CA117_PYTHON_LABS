#!/usr/bin/env python3

import sys

token = sys.argv[1]
try:
    with open(token) as fd:
        c = ['1']
        v = ['']
        count = 0
        fd = fd.readlines()

        for line in fd:
            line = line.strip()
            try:
                e = line[0:2]
                if int(e) > int(c[0]):
                    c.pop(0)
                    c.append(e)
                    v.pop(0)
                    v.append(line[3:])
            except ValueError:
                print("Invalid mark", line[0] + '' + line[1], "encountered. Exiting.")
                break
            finally:
                count += 1

        if count == len(line):
            print('Best student:', v[0])
            print('Best mark:', c[0])

except FileNotFoundError:
    print("The file", file, "could not be opened.")
