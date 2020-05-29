#!/usr/bin/env python3

def count_letters(n):
    if n == '':
        return 0

    else:
        return len(n)

def main():
    len = None
    print(count_letters('cat'))
    print(count_letters('catastrophe'))
    print(count_letters(''))

if __name__ == '__main__':
    main()
