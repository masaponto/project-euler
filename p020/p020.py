#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def solve(n):
    return sum(map(int,str(math.factorial(n))))

def main():
    print(solve(100))

if __name__ == "__main__":
    main()
