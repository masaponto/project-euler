#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def get_prime(n):
    plist = []
    slist = list(range(2, n))

    while True:
        m = slist.pop(0)
        plist.append(m)

        for i in slist:
            if i % m == 0:
                slist.remove(i)

        if len(slist) == 0 or slist[0] == int(math.sqrt(m) + 0.5):
            break

    return plist


def solve(n):
    return sum(get_prime(n))


def solve_(n):
    plist = [2]
    m = 3
    while m < n:
        pflag = False

        for p in plist:
            if m % p == 0:
                pflag = True

        if not pflag:
            plist.append(m)

        m += 2

    return sum(plist)


def hoge(n):
    slist = list(range(3, n, 2))

    nplist = []
    for m in slist:
        for j in range(2, m):
            if m % j == 0:
                nplist.append(m)
                break

    return 2 + sum(slist) - sum(nplist)


def main():
    # print(hoge(10))
    #print(hoge(2000000))
    print(solve_(2000000))

if __name__ == "__main__":
    main()
