#!/usr/bin/python3

from aoc import *


def solve(input_str: str):
    grid = parse_list(input_str, lambda x: lmap(int, x))
    H = len(grid)
    W = len(grid[0])

    heads = {}
    head_id = 0
    for y in range(H):
        for x in range(W):
            if grid[y][x] == 0:
                heads[(x, y)] = Counter({head_id: 1})
                head_id += 1

    steps = [heads]
    for i in range(1, 10):
        next_step = defaultdict(Counter)
        for (x, y), ids in steps[-1].items():
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < W and 0 <= ny < H:
                    if grid[ny][nx] == i:
                        next_step[(nx, ny)] += ids
        steps.append(next_step)

    part1 = Counter()
    part2 = Counter()
    for v in steps[-1].values():
        part1.update(v.keys())
        part2.update(v)

    return sum(part1.values()), sum(part2.values())


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (796, 1942)


if __name__ == "__main__":
    main()
