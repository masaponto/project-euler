#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


def get_score(i, name):
    return i * sum(list(map(lambda c: ord(c) - ord('A') + 1, name)))


def solve():
    with open('p022_names.txt', 'r') as name_file:
        reader = csv.reader(name_file)
        names = list(reader)[0]

    names.sort()

    scores = [get_score(i + 1, name) for i, name in enumerate(names)]
    return sum(scores)


def main():
    print(get_score(938, 'COLIN'))
    print(solve())


if __name__ == "__main__":
    main()
