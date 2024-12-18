#!/usr/bin/python3

from aoc import *
import heapq


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
    grid = [[0 for _ in range(W)] for _ in range(H)]
    for mx, my in meteorbytes[:INITIAL_STEPS]:
        grid[my][mx] = 1

    short = shortest(grid)
    part1 = len(short) - 1

    for mx, my in meteorbytes[INITIAL_STEPS:]:
        grid[my][mx] = 1
        if (mx, my) not in short:
            continue
        short = shortest(grid)
        if not short:
            part2 = f"{mx},{my}"
            break

    return (part1, part2)


def shortest(grid):
    H, W = 71, 71
    start = (0, 0)
    end = (W - 1, H - 1)
    paths = [(1, start, {start})]
    min_len = defaultdict(lambda: float("inf"))

    def should_quit(x, y, l):
        if min_len[(x, y)] <= l:
            return True
        else:
            min_len[(x, y)] = l
            return False

    def get_neighs(x, y, visited):
        if (x, y) == end:
            return []
        return [
            (x + dx, y + dy)
            for dx, dy in DIRS
            if (
                (0 <= y + dy < H)
                and (0 <= x + dx < W)
                and grid[y + dy][x + dx] == 0
                and (x + dx, y + dy) not in visited
            )
        ]

    while paths:
        _, (x, y), visited = heapq.heappop(paths)

        if (x, y) == end:
            return visited

        if should_quit(x, y, len(visited)):
            continue

        # silly optimization got me 25% faster
        while neighs := get_neighs(x, y, visited):
            for nx, ny in neighs[1:]:
                new_visited = set(visited)
                new_visited.add((nx, ny))
                heapq.heappush(paths, (len(new_visited), (nx, ny), new_visited))

            # basically instead of pushing and popping every time. advance the current x,y and only pop a new point when you can't move anymore
            x, y = neighs[0]
            visited.add(neighs[0])
            # of course quit if we're too long
            if should_quit(x, y, len(visited)):
                break
        else:
            if (x, y) == end:
                # if we hit the end, we need to make sure its the shortest by putting it on the heap
                heapq.heappush(paths, (len(visited), (x, y), visited))


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (370, "65,6")


if __name__ == "__main__":
    main()
