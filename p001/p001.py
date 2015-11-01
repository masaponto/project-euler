#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(n):
    return sum( [i for i in range(n) if i % 3 == 0 or i % 5 == 0 ])

def main():
    print(solve(1000))

if __name__ == "__main__":
    main()
