#!/usr/bin/python3

from aoc import *


def solve(input_str):
    g = parse_grid(input_str, int)
    part1 = sum(good(r) for r in g)
    part2 = sum(ggood(r) for r in g)

    return (part1, part2)


def good(r):
    s = set(j - k for j, k in window(r, 2))
    return all(-3 <= ss < 0 for ss in s) or all(0 < ss <= 3 for ss in s)


def ggood(r):
    for i in range(len(r)):
        newr = list(r)
        newr.pop(i)
        if good(newr):
            return True
    return False


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (631, 665)


if __name__ == "__main__":
    main()
