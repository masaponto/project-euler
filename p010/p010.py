#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(n):
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


def main():
    print(solve(10))
    print(solve(2000000))

if __name__ == "__main__":
    main()
