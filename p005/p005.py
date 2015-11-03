#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce


def gcd(m: int, n: int) -> int:
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


def lcm(m: int, n: int) -> int:
    return (m * n) // gcd(m, n)


def solve(n: int) -> int:
    return reduce(lambda x, y: lcm(x, y), list(range(1, n)))


def main():
    print(solve(20))


if __name__ == "__main__":
    main()
