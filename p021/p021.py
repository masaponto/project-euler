#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy.ntheory import factorint


def d(n):
    factors = factorint(n)
    s = 1
    for p, i in factors.items():
        s *= sum([p**n for n in range(i + 1)])
    return s - n


def solve():
    s = [n for n in range(2, 10000) if n == d(d(n)) and n != d(n)]
    print(s)
    print(sum(s))


def main():
    solve()

if __name__ == "__main__":
    main()
