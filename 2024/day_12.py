#!/usr/bin/python3

from aoc import *


def solve(input_str: str):
    g = parse_list(input_str, list)
    H = len(g)
    W = len(g[0])
    regions = []
    for y in range(H):
        for x in range(W):
            if g[y][x] == None:
                continue
            new_region = {(x, y)}
            val = g[y][x]
            flood(g, x, y, new_region, val)
            regions.append(new_region)

    part1 = 0
    part2 = 0
    for plants in regions:
        area = len(plants)
        perimeter = area * 4
        sides = 0
        for x, y in plants:
            perimeter -= sum(
                s in plants for s in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
            )
            corners = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dx, dy in corners:
                side1 = (x + dx, y)
                side2 = (x, y + dy)
                corner = (x + dx, y + dy)
                match (side1 in plants, corner in plants, side2 in plants):
                    case (False, _, False):
                        # outer corner
                        sides += 1

                    case (True, False, True):
                        # inner corner
                        sides += 1

        part1 += area * perimeter
        part2 += area * sides

    return (part1, part2)


def flood(grid, x, y, region, val):
    H = len(grid)
    W = len(grid[0])
    grid[y][x] = None
    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if 0 <= nx < W and 0 <= ny < H:
            if grid[ny][nx] == val:
                region.add((nx, ny))
                flood(grid, nx, ny, region, val)


def trace(region):
    outline = []
    for x, y in region:
        sides = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
        if any(side not in region for side in sides):
            outline.append((x, y))


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1473276, 901100)


if __name__ == "__main__":
    main()
