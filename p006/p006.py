#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pow_sum(n):
    return sum([i**2 for i in range(1, n + 1)])


def sum_pow(n):
    return sum(list(range(1, n + 1)))**2


def solve(n):
    return sum_pow(n) - pow_sum(n)


def main():
    print(solve(100))

if __name__ == "__main__":
    main()
