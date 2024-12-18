#!/usr/bin/python3

from aoc import *


DIRS = (
    (0, -1),  # ^
    (1, 0),  # >
    (0, 1),  # v
    (-1, 0),  # <
)


def solve(input_str: str):
    meteorbytes = chunk(ints(input_str), 2)
    INITIAL_STEPS = 1024
    H, W = 71, 71

    def make_grid(steps):
        grid = [[0 for _ in range(W)] for _ in range(H)]
        for mx, my in meteorbytes[:steps]:
            grid[my][mx] = 1
        return grid

    short = shortest(make_grid(INITIAL_STEPS))
    part1 = len(short) - 1

    low = 1024
    high = len(meteorbytes)
    # not convinced this is perfectly correct
    while low < high:
        if meteorbytes[low - 1] not in short:
            low += 1
            continue
        mid = (low + high) // 2
        if maybe := shortest(make_grid(mid)):
            short = maybe
            low = mid + 1
        else:
            high = mid

    mx, my = meteorbytes[low - 1]
    part2 = f"{mx},{my}"

    return (part1, part2)


def shortest(grid):
    H, W = 71, 71
    start = (0, 0)
    end = (W - 1, H - 1)
    been_to = {start}
    points = [(start, {start})]

    def get_neighs(x, y):
        return [
            (x + dx, y + dy)
            for dx, dy in DIRS
            if (
                (0 <= y + dy < H)
                and (0 <= x + dx < W)
                and grid[y + dy][x + dx] == 0
                and (x + dx, y + dy) not in been_to
            )
        ]

    while points:
        new_points = []
        for (x, y), path in points:
            if (x, y) == end:
                return path
            for nx, ny in get_neighs(x, y):
                new_path = set(path)
                new_path.add((nx, ny))
                new_points.append(((nx, ny), new_path))
                been_to.add((nx, ny))
        points = new_points


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (370, "65,6")


if __name__ == "__main__":
    main()
