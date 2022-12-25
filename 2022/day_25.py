#!/usr/bin/python3

from aoc import *
import math

M = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
def snafu_to_int(n):
    r = 0

    for i in n:
        r = r * 5 + M[i]

    return r

def int_to_snafu(n):
    r = ""

    while n != 0:
        m = n % 5
        m = m - (m > 2) * 5
        n = (n - m) // 5
        r = '=-012'[m + 2] + r

    return r

def solve(input_str):
    s = sum(map(snafu_to_int, lines(input_str)))
    return int_to_snafu(s)

def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == '2=-0=01----22-0-1-10'

if __name__ == '__main__':
    main()

