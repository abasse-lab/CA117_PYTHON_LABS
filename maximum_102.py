#!/usr/bin/env python3

def maximum(n):
    if n == []:
        return None

    else:
        return max(n)

def main():
    max = None
    print(maximum([6, 5, 1, 3, 4]))
    print(maximum([6, 5, 11, 3, 4]))
    print(maximum([6, 15, 11, 13, 14]))
    print(maximum([6, 15, 11, 13, 4]))

if __name__ == '__main__':
    main()
