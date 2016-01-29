#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_leap(year):
    if year % 4 == 0:
        return not (year % 400 != 0 and year % 100 == 0)
    return False


def solve():
    count = 0

    day30_month = (9, 4, 6, 11)
    d_week = 0

    for year in range(1900, 2000 + 1):
        for month in range(1, 12 + 1):
            for day in range(1, 31 + 1):
                d_week = (d_week + 1) % 7

                if month in day30_month and day is 30:
                    continue
                if month is 2 and day is 29 and is_leap(year):
                    continue
                elif month is 2 and day is 28 and not is_leap(year):
                    continue

                if 1901 <= year <= 2000 and day is 1 and d_week is 0:
                    count += 1

    return count


def main():
    ans = solve()
    print(ans)


if __name__ == "__main__":
    main()
