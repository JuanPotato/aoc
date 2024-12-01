#!/usr/bin/python3

from aoc import *


def solve(input_str):
    l, r = every_n(ints(input_str), 2)
    l.sort()
    r.sort()
    part1 = sum(abs(ll - rr) for ll, rr in zip(l, r))
    rr = Counter(r)
    part2 = sum(ll * rr[ll] for ll in l)

    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (2742123, 21328497)


if __name__ == "__main__":
    main()
