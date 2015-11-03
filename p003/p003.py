#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(n, pflist):
    for i in range(2,n+1):
        if n % i == 0:
            pflist.append(i)
            solve(int(n/i), pflist)
            break

    return pflist


def main():
    n = 600851475143
    pflist = []
    print(solve(n, pflist))
    print(max(solve(n, pflist)))
if __name__ == "__main__":
    main()
