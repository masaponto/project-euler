#!/usr/bin/env python
# -*- coding: utf-8 -*-

def triangular(n):
    return int(n * (n + 1) / 2)

def get_divisor(n):
    i = 1
    dlist = []

    while i*i <= n:
        if n % i == 0:
            dlist.append(i)
            if i != n/i:
                dlist.append(int(n/i))
        i += 1

    return dlist


def solve():
    n = 1

    while True:
        t = triangular(n)
        if t > 500:
            if len(get_divisor(t)) > 500:
                break
        n += 1
    return t

def main():

    print(solve())



if __name__ == "__main__":
    main()
