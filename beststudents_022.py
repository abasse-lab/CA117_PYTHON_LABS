#!/usr/bin/env python3

import sys
import operator

def best(s):
    d = {" ".join(line[1:]) : int(line[0]) for line in s}
    k = max(d.items() , key = operator.itemgetter(1))
    name_list = ", ".join([name for name in d.keys() if d[name] == k[1]])
    return "Best student(s): {}\nBest mark: {}".format(name_list , k[1])

def main():
    try:
        s = open(sys.argv[1] , 'r')
        a = [line.split() for line in s]
        for line in a:
            try:
                line[0] = int(line[0])
            except:
                print("Invalid mark" , line[0] , "encountered. Skipping.")
                a.remove(line)
        print(best(a))
        s.close()
    except FileNotFoundError:
        print("The file" , sys.argv[1] , "could not be opened.")

if __name__ == "__main__":
    main()
   