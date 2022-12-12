#!/usr/bin/python3

from aoc import *

def solve(input_str):
    return (hike(input_str), hike(input_str))

def hike(input_str, call_count=[0]):
    # just did this bit for fun
    call_count[0] += 1
    part2 = call_count[0] == 2


    for yi, r in enumerate(lines(input_str)):
        if 'S' in r:
            start = Point(r.index('S'), yi)
        if 'E' in r:
            end = Point(r.index('E'), yi)

    grid = [[int(c, 36) - int('a',36) for c in r] for r in lines(input_str.replace('S','a').replace('E','z'))]

    paths = [(end,)]
    visited = {end}

    while paths:
        p = paths.pop(0)
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            pp = p[-1]
            np = Point(pp.x + dx, pp.y + dy)

            if not (0 <= np.x < len(grid[0]) and 0 <= np.y < len(grid)):
                continue
            if np in visited:
                continue
            if grid[pp.y][pp.x] - grid[np.y][np.x] > 1:
                continue

            if [np == start, grid[np.y][np.x] == 0][part2]:
                return len(p)

            paths.append(p + (np,))
            visited.add(np)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (504, 500)

if __name__ == '__main__':
    main()


