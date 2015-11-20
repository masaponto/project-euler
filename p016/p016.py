#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(n):
    return sum(list(map(int,str(2**n))))

def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
