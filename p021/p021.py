#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy.ntheory import factorint
from functools import reduce


def mat(lst):
    return reduce(lambda x, y: x*y, lst, 1)

def d(n):
    return mat([sum([p**n for n in range(i + 1)]) for p, i in factorint(n).items()]) - n

def solve():
    s = [n for n in range(2, 10000) if n == d(d(n)) and n != d(n)]
    print(s)
    print(sum(s))


def main():
    solve()

if __name__ == "__main__":
    main()
