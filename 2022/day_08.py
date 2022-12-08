#!/usr/bin/python3

from aoc import *
import re

def solve(input_str):
    grid = [lmap(int, l) for l in lines(input_str)]
    visible = len(grid) * 2 + len(grid[0]) * 2 - 4
    scenic = 0

    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            can_see = False
            can_see |= all(grid[r2][c] < grid[r][c] for r2 in make_range(r-1, 0)) # up
            can_see |= all(grid[r2][c] < grid[r][c] for r2 in make_range(r+1, len(grid) - 1)) # down
            can_see |= all(grid[r][c2] < grid[r][c] for c2 in make_range(c-1, 0)) # left
            can_see |= all(grid[r][c2] < grid[r][c] for c2 in make_range(c+1, len(grid[0]) - 1)) # right
            visible += can_see

            up,do,le,ri = 0,0,0,0

            for r2 in make_range(r-1, 0):
                up += 1
                if int(grid[r2][c]) >= int(grid[r][c]): break

            for r2 in make_range(r+1, len(grid) - 1):
                do += 1
                if int(grid[r2][c]) >= int(grid[r][c]): break

            for c2 in make_range(c-1, 0):
               le += 1
               if int(grid[r][c2]) >= int(grid[r][c]): break

            for c2 in make_range(c+1, len(grid[0]) - 1):
               ri += 1
               if int(grid[r][c2]) >= int(grid[r][c]): break

            scenic = max(up*do*le*ri, scenic)

    return (visible, scenic)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1703, 496650)

if __name__ == '__main__':
    main()


