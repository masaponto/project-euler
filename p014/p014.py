#!/usr/bin/env python
# -*- coding: utf-8 -*-

def collatz(n, lst):
    lst.append(n)

    if n == 1:
        return lst

    elif n % 2 == 0:
        return collatz(int(n/2), lst)

    else:
        return collatz(3*n + 1, lst)


def solve(n):
    m = 0


    for i in range(13, n):
        l = len(collatz(i, []))
        if m < l:
            j = i
            m = l

    return j

def main():
    #print(collatz(13, []))
    print(solve(1000000))



if __name__ == "__main__":
    main()
