#!/usr/bin/python3

from aoc import *
import numpy as np


def solve(input_str):
    g = np.array([list(r) for r in input_str.split("\n")])
    return part1(g), part2(g)


def part1(g):
    # diagonals
    search = [g[::-1, :].diagonal(i) for i in range(-g.shape[0] + 1, g.shape[1])]
    search.extend(g.diagonal(i) for i in range(g.shape[1] - 1, -g.shape[0], -1))

    # rows & cols
    search.extend(g)
    search.extend(np.transpose(g))

    return sum("".join(w) in ("XMAS", "SAMX") for r in search for w in window(r, 4))


def part2(g):
    count = 0
    for r in range(len(g) - 2):
        for c in range(len(g[0]) - 2):
            gg = g[r : r + 3, c : c + 3]
            f = gg[0, 0] + gg[1, 1] + gg[2, 2]
            b = gg[2, 0] + gg[1, 1] + gg[0, 2]
            good = ("MAS", "SAM")
            if f in good and b in good:
                count += 1
    return count


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (2427, 1900)


if __name__ == "__main__":
    main()
