#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve() -> int:
    for i in range(1, 1000 - 2):
        for j in range(i + 1, 1000 - 2 - i):
            for k in range(j + 1, 1000 - 2 - j):
                if (i**2 + j**2 == k**2 and i + j + k == 1000):
                    return i * j * k
    return 0


def main():
    print(solve())


if __name__ == "__main__":
    main()
