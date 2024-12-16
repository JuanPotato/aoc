#!/usr/bin/python3

from aoc import *
import heapq


DIRS = (
    (0, -1),  # ^
    (1, 0),  # >
    (0, 1),  # v
    (-1, 0),  # <
)
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def turn_count(d1, d2):
    dif = abs(d1 - d2)
    return min(dif, 4 - dif)


def solve(input_str: str):
    grid = parse_list(input_str, list)
    H = len(grid)
    W = len(grid[0])
    end = find_me(grid, "E")
    start = find_me(grid, "S")
    paths = [(0, start, EAST, {start})]
    min_costs = {(0, 0, EAST): 0}
    best_cost = float("inf")
    best_tiles = {}

    def add_cost(x, y, d, cost):
        for nd in range(4):
            ncost = cost + turn_count(d, nd) * 1000
            key = (x, y, nd)
            min_costs[key] = min(min_costs.get(key, float("inf")), ncost)

    while paths:
        cost, (x, y), d, visited = heapq.heappop(paths)
        if min_costs.get((x, y, d), float("inf")) < cost:
            continue
        else:
            add_cost(x, y, d, cost)

        if (x, y) == end:
            if cost == best_cost:
                best_tiles.update(visited)
            if cost < best_cost:
                best_cost = min(
                    min_costs.get((*end, i), float("inf")) for i in range(4)
                )
                best_tiles = visited
            continue

        neighs = [
            ((x + dx, y + dy), d)
            for d, (dx, dy) in enumerate(DIRS)
            if (grid[y + dy][x + dx] != "#" and (x + dx, y + dy) not in visited)
        ]

        while neighs:
            for (nx, ny), nd in neighs[1:]:
                new_visited = set(visited)
                new_visited.add((nx, ny))
                ncost = cost + turn_count(d, nd) * 1000 + 1
                heapq.heappush(paths, (ncost, (nx, ny), nd, new_visited))

            (x, y), nd = neighs[0]
            cost += turn_count(d, nd) * 1000 + 1
            visited.add((x, y))
            d = nd
            if min_costs.get((x, y, d), float("inf")) < cost:
                break
            else:
                add_cost(x, y, d, cost)
            if (x, y) == end:
                if cost == best_cost:
                    best_tiles.update(visited)
                if cost < best_cost:
                    best_cost = min(
                        min_costs.get((*end, i), float("inf")) for i in range(4)
                    )
                    best_tiles = visited
                break

            neighs = [
                ((x + dx, y + dy), d)
                for d, (dx, dy) in enumerate(DIRS)
                if (grid[y + dy][x + dx] != "#" and (x + dx, y + dy) not in visited)
            ]
        else:
            if (x, y) == end:
                if cost == best_cost:
                    best_tiles.update(visited)
                if cost < best_cost:
                    best_cost = min(
                        min_costs.get((*end, i), float("inf")) for i in range(4)
                    )
                    best_tiles = visited

    return (best_cost, len(best_tiles))


def find_me(grid, v):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == v:
                return (x, y)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (89460, 504)


if __name__ == "__main__":
    main()
