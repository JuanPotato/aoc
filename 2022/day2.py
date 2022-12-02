#!/usr/bin/python3

from aoc import *

def solve(input_str):
    p1, p2 = 0, 0

    for a, b in parse_grid(input_str, str):
        a = ord(a) - ord('A')
        b = ord(b) - ord('X')
        c = ((b - 1) + a) % 3

        # Future me is going to be so confused hahaha
        p1 += 3 * ((b - a + 1) % 3) + (b + 1)
        p2 += 3 * ((c - a + 1) % 3) + (c + 1)

    return (p1, p2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (14264, 12382)

if __name__ == '__main__':
    main()


