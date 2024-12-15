#!/usr/bin/python3

from aoc import *


DIRS = {"v": (0, 1), "^": (0, -1), ">": (1, 0), "<": (-1, 0)}


def solve(input_str: str):
    grid_str, dirs = input_str.strip().split("\n\n")
    dirs = dirs.replace("\n", "")
    grid = parse_list(grid_str, list)
    x, y = find_me(grid, "@")

    for d in dirs:
        x, y = move_basic(grid, x, y, d)

    part1 = 0
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "O":
                part1 += y * 100 + x

    grid2_str = (
        grid_str.replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )
    grid2 = parse_list(grid2_str, list)
    x, y = find_me(grid2, "@")
    for d in dirs:
        if d in "<>":
            x, y = move_basic(grid2, x, y, d)
        else:
            x, y = move_wide_up_down(grid2, [(x, y)], d)[0]

    part2 = 0
    for y, row in enumerate(grid2):
        for x, val in enumerate(row):
            if val == "[":
                part2 += y * 100 + x

    return (part1, part2)


def move_basic(grid, x, y, d):
    dx, dy = DIRS[d]
    nx = x + dx
    ny = y + dy
    if grid[ny][nx] in "O[]":
        move_basic(grid, nx, ny, d)
    if grid[ny][nx] == ".":
        grid[ny][nx] = grid[y][x]
        grid[y][x] = "."
        return nx, ny
    return x, y


def move_wide_up_down(grid, blocks, d):
    dx, dy = DIRS[d]
    next_blocks = [(x + dx, y + dy) for x, y in blocks]

    # can't move
    if any(grid[ny][nx] == "#" for nx, ny in next_blocks):
        return blocks

    # move boxes
    if any(grid[ny][nx] in "[]" for nx, ny in next_blocks):
        blocks_to_move = set()
        for nx, ny in next_blocks:
            if grid[ny][nx] == "[":
                blocks_to_move.add((nx, ny))
                blocks_to_move.add((nx + 1, ny))
            if grid[ny][nx] == "]":
                blocks_to_move.add((nx - 1, ny))
                blocks_to_move.add((nx, ny))
        move_wide_up_down(grid, blocks_to_move, d)

    # can move
    if all(grid[ny][nx] == "." for nx, ny in next_blocks):
        for (x, y), (nx, ny) in zip(blocks, next_blocks):
            grid[ny][nx] = grid[y][x]
            grid[y][x] = "."
        return next_blocks

    return blocks


def find_me(grid, v):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == v:
                return (x, y)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1294459, 1319212)


if __name__ == "__main__":
    main()
