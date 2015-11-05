#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(n: int) -> int:
    plist = [2]
    m = 3
    while True:
        pflag = False

        for p in plist:
            if m % p == 0:
                pflag = True

        if not pflag:
            plist.append(m)

        m += 2

        if len(plist) == n:
            break

    return plist[n - 1]


def main():

    print(solve(6))
    print(solve(10001))

if __name__ == "__main__":
    main()
