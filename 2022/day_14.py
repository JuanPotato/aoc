#!/usr/bin/python3

from aoc import *
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

def solve(input_str):
    # My brain is currently a hamster trying to run a marathon, I'm not going to try and make this simpler
    return part1(input_str), part2(input_str)

def part1(a):
    xs = ints(a)[::2] + [500]
    ys = ints(a)[1::2] + [0]

    xrange = min(xs),max(xs)
    yrange = min(ys),max(ys)

    cave = [['.' for _ in make_range(*xrange)] for _ in make_range(*yrange)]
    def gcave(x,y):
        return cave[y - yrange[0]][x - xrange[0]]
    def scave(x,y,v):
        cave[y - yrange[0]][x - xrange[0]] = v

    for rock in lines(a):
        coords = list(zip(ints(rock)[::2], ints(rock)[1::2]))
        for start,end in window(coords, 2):
            for rx in make_range(start[0], end[0]):
                for ry in make_range(start[1], end[1]):
                    scave(rx, ry, '#')

    def drop_sand():
        sand = Point(500, 0)
        #scave(*sand, '+')

        while xrange[0] <= sand.x <= xrange[1] and yrange[0] <= sand.y <= yrange[1]:
            if sand.y + 1 > yrange[1] or gcave(sand.x, sand.y + 1) == '.':
                sand.y += 1

            elif sand.x - 1 < xrange[0] or sand.y + 1 > yrange[1] or gcave(sand.x - 1, sand.y + 1) == '.':
                sand.x -= 1
                sand.y += 1

            elif sand.x + 1 > xrange[1] or sand.y + 1 > yrange[1] or gcave(sand.x + 1, sand.y + 1) == '.':
                sand.x += 1
                sand.y += 1

            else:
                scave(sand.x, sand.y, '+')
                break
        else:
            return False
        return True

    c = 0

    while drop_sand():
        c += 1

    return c

def part2(a):
    xs = ints(a)[::2] + [500]
    ys = ints(a)[1::2] + [0]

    xrange = [min(xs),max(xs)]
    yrange = [min(ys),max(ys)]

    xrange[0] -= 200 # eh good enough
    xrange[1] += 200
    yrange[1] += 2

    floor = f'\n{xrange[0]},{yrange[1]} -> {xrange[1]},{yrange[1]}'

    cave = [['.' for _ in make_range(*xrange)] for _ in make_range(*yrange)]
    def gcave(x,y):
        return cave[y - yrange[0]][x - xrange[0]]
    def scave(x,y,v):
        cave[y - yrange[0]][x - xrange[0]] = v

    for rock in lines(a + floor):
        coords = list(zip(ints(rock)[::2], ints(rock)[1::2]))
        for start,end in window(coords, 2):
            for rx in make_range(start[0], end[0]):
                for ry in make_range(start[1], end[1]):
                    scave(rx, ry, '#')

    def drop_sand():
        sand = Point(500, 0)

        if gcave(sand.x, sand.y) != '.':
            return False

        while xrange[0] <= sand.x <= xrange[1] and yrange[0] <= sand.y <= yrange[1]:
            if sand.y + 1 > yrange[1] or gcave(sand.x, sand.y + 1) == '.':
                sand.y += 1

            elif sand.x - 1 < xrange[0] or sand.y + 1 > yrange[1] or gcave(sand.x - 1, sand.y + 1) == '.':
                sand.x -= 1
                sand.y += 1

            elif sand.x + 1 > xrange[1] or sand.y + 1 > yrange[1] or gcave(sand.x + 1, sand.y + 1) == '.':
                sand.x += 1
                sand.y += 1

            else:
                scave(sand.x, sand.y, '+')
                break
        else:
            return False
        return True

    c = 0

    while drop_sand():
        c += 1

    return c


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (994, 26283)

if __name__ == '__main__':
    main()


