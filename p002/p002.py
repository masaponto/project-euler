#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(n: int) -> int:
    a, b = 1, 2
    s = 0

    while a < n:
        if a % 2 == 0:
            s += a
        a, b = b, a+b

    return s

def main():
    print(solve(4000000))

if __name__ == "__main__":
    main()
