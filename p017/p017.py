#!/usr/bin/env python
# -*- coding: utf-8 -*-

def first(cs):
    assert(len(cs) == 1)

    dic = { '0': '',
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine' }

    return dic[cs]

def second(cs):
    assert(len(cs) == 2)

    dic = { '0': '',
            '2': 'twenty',
            '3': 'thirty',
            '4': 'forty',
            '5': 'fifty',
            '6': 'sixty',
            '7': 'seventy',
            '8': 'eighty',
            '9': 'ninety'}

    idic = { '00': '',
             '10': 'ten',
             '11': 'eleven',
             '12': 'twelve',
             '13': 'thirteen',
             '14': 'fourteen',
             '15': 'fifteen',
             '16': 'sixteen',
             '17': 'seventeen',
             '18': 'eighteen',
             '19': 'nineteen'}

    if cs[0] == '1':
        return idic[cs]

    return dic[ cs[0] ] + first(cs[1])


def third(cs):
    assert(len(cs) == 3)

    if cs[1:3] == '00':
        return first(cs[0]) + 'hundred'

    return first(cs[0]) + 'hundredand' + second(cs[1:3])

def fourth(cs):
    assert(len(cs) == 4)
    return first(cs[0]) + 'thousand'

def num2word(cs):
    n = len(cs)

    if n == 1:
        return first(cs)
    elif n == 2:
        return second(cs)
    elif n == 3:
        return third(cs)
    else:
        return fourth(cs)

def solve(n):
    s = list(map(str, list(range(1, n + 1))))
    return len("".join(list(map(num2word, s))))


def main():
    print(num2word('342'), len(num2word('342')))
    print(num2word('115'), len(num2word('115')))

    print(solve(5))
    print(solve(1000))


if __name__ == "__main__":
    main()
