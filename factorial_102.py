#!/usr/bin/env python3

def factorial(n):
    if n == 0:
        return 1
    else:
        x = 1
        for i in range(1, n + 1):
            x = x * i
        return x

def main():
    print(factorial(0))
    print(factorial(1))
    print(factorial(12))

if __name__ == '__main__':
    main()
