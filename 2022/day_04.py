#!/usr/bin/python3

from aoc import *

def solve(input_str):
    p1, p2 = 0, 0

    for l in lines(input_str):
        s1, e1, s2, e2 = ints(l)

        p1 += (s1 <= s2 <= e2 <= e1) or (s2 <= s1 <= e1 <= e2)
        p2 += not ((s1 > e2) or (s2 > e1))

    return (p1, p2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (657, 938)

if __name__ == '__main__':
    main()


