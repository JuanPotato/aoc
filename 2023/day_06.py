#!/usr/bin/python3

from aoc import *
from math import *


def solve(input_str):
    part1 = 1
    for k in (d(T, D) for T, D in zip(*list(map(ints, input_str.split("\n"))))):
        part1 *= k
    part2 = d(*ints(input_str.replace(" ", "")))
    return (part1, part2)


def d(T, D):
    f = sqrt(T * T - 4 * D)
    return floor((T + f) / 2) - ceil((T - f) / 2) + 1


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (449550, 28360140)


if __name__ == "__main__":
    main()
