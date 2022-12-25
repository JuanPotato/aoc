#!/usr/bin/python3

from aoc import *
import math

def solve(input_str):
    m = {
        '2': 2,
        '1': 1,
        '0': 0,
        '-': -1,
        '=': -2
    }

    s = 0
    for l in lines(input_str):
        b = 1
        n = 0
        for d in l[::-1]:
            n += m[d] * b
            b *= 5
        s += n

    return snafu(s)

def snafu(n):
    digits = 1
    max_num = lambda d: sum(2*5**i for i in range(d))
    while max_num(digits) < n:
        digits += 1

    num = []
    m = 0
    for i in make_range(digits-1, 0):
        nd = 0
        err = math.inf
        for k in (-2, -1, 0, 1, 2):
            v = k * 5**i
            nerr = abs(n - (m + v))
            if nerr < err:
                err = nerr
                nd = k
        m += nd * 5**i
        num.append(nd)
    return ''.join('=-012'[o+2] for o in num)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == '2=-0=01----22-0-1-10'

if __name__ == '__main__':
    main()


