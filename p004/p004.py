#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_palindrome(n: int) -> bool:
    """
    >>> is_palindrome(1001)
    True
    >>> is_palindrome(1221)
    True
    >>> is_palindrome(1234)
    False
    >>> is_palindrome(9234)
    False

    """

    s = str(n)
    for i in range(int(len(s)/2)):
        if s[i] != s[-(i+1)]:
            return False
    return True


def solve() -> int:
    pal_list = []

    for i in range(100, 999 + 1):
        for j in range(100, 999 + 1):
            m = i*j
            if is_palindrome(m):
                pal_list.append(m)

    return max(pal_list)


def main():
    print(solve())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
