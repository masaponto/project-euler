#!/usr/bin/env python
# -*- coding: utf-8 -*-

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def solve(n):
    return factorial(n*2) // (factorial(n) * factorial(n))

def main():
    print(solve(20))

if __name__ == "__main__":
    main()
