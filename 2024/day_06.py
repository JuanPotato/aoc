#!/usr/bin/python3

from aoc import *


def solve(input_str: str):
    grid = list(parse_list(input_str, list))
    part1, visited = travel([list(r) for r in grid])

    part2 = 0
    for (c, r) in visited:
        if grid[r][c] == ".":
            new_grid = [list(r) for r in grid]
            new_grid[r][c] = "#"
            if travel(new_grid) == None:
                part2 += 1
    return part1, part2


def travel(grid):
    x, y = next(
        (x, y) for y, row in enumerate(grid) for x, val in enumerate(row) if val == "^"
    )

    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    nums = [1, 2, 4, 8]
    d = 0
    grid[y][x] = nums[d]

    loop = False
    while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        dx, dy = dirs[d]
        if not (0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid)):
            break

        match grid[y + dy][x + dx]:
            case "#":
                d = (d + 1) % 4

            case v:
                y += dy
                x += dx
                if v == ".":
                    grid[y][x] = nums[d]
                else:
                    if grid[y][x] & nums[d]:
                        return None
                    grid[y][x] |= nums[d]

    visited = [
        (x, y)
        for y, row in enumerate(grid)
        for x, v in enumerate(row)
        if isinstance(v, int)
    ]
    return sum(isinstance(v, int) for r in grid for v in r), visited


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (5030, 1928)


if __name__ == "__main__":
    main()
