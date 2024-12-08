#!/usr/bin/python3

from aoc import *
import itertools


def solve(input_str: str):
    grid = parse_list(input_str, str)
    H = len(grid)
    W = len(grid[0])
    antennas = defaultdict(list)
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val != ".":
                antennas[val].append((x, y))

    part1 = set()
    part2 = set()
    for freq, locs in antennas.items():
        for b, c in itertools.combinations(locs, 2):
            dx = c[0] - b[0]
            dy = c[1] - b[1]

            a = (b[0] - dx, b[1] - dy)
            d = (c[0] + dx, c[1] + dy)
            for xx, yy in (a, d):
                if 0 <= xx < W and 0 <= yy < H:
                    part1.add((xx, yy))

            xx, yy = b
            while 0 <= xx < W and 0 <= yy < H:
                part2.add((xx, yy))
                xx -= dx
                yy -= dy

            xx, yy = c
            while 0 <= xx < W and 0 <= yy < H:
                part2.add((xx, yy))
                xx += dx
                yy += dy

    return len(part1), len(part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (311, 1115)


if __name__ == "__main__":
    main()
