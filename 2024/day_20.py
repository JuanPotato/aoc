#!/usr/bin/python3

from aoc import *

DIRS = (
    (0, -1),  # ^
    (1, 0),  # >
    (0, 1),  # v
    (-1, 0),  # <
)

SKIPS = (
    # straight 2
    (0, -2),
    (2, 0),
    (0, 2),
    (-2, 0),
)


def solve(input_str: str):
    grid = parse_list(input_str, list)
    H = len(grid)
    W = len(grid[0])
    end = find_me(grid, "E")
    start = find_me(grid, "S")
    grid[start[1]][start[0]] = 0
    grid[end[1]][end[0]] = "."
    path = [start]
    x, y = start
    i = 0
    while (x, y) != end:
        x, y = next((nx, ny) for nx, ny in neighbors(x, y, W, H) if grid[ny][nx] == ".")
        grid[y][x] = (i := i + 1)
        path.append((x, y))

    part1 = cheat(grid, path, 2)
    part1 = sum(v for k, v in part1.items() if k >= 100)

    part2 = cheat(grid, path, 20)
    part2 = sum(v for k, v in part2.items() if k >= 100)

    return (part1, part2)


def cheat(grid, path, ps):
    H = len(grid)
    W = len(grid[0])
    deltas = list(points_within(0, 0, ps))
    cheater = Counter()

    for pi, (px, py) in enumerate(path):
        for dx, dy in deltas:
            hx = px + dx
            hy = py + dy
            if not (0 <= hx < W and 0 <= hy < H):
                continue
            if grid[hy][hx] == "#":
                continue
            saved = grid[hy][hx] - pi - abs(dx) - abs(dy)
            if saved > 0:
                cheater[saved] += 1

    return cheater


def neighbors(x, y, W, H):
    return [
        (x + dx, y + dy) for dx, dy in DIRS if ((0 <= y + dy < H) and (0 <= x + dx < W))
    ]


def points_within(x, y, d):
    for dy in range(-d, d + 1):
        adx = d - abs(dy)
        for dx in range(-adx, adx + 1):
            if (dx, dy) == (0, 0):
                continue
            yield (x + dx, y + dy)


def find_me(grid, v):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == v:
                return (x, y)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1497, 1030809)


if __name__ == "__main__":
    main()
