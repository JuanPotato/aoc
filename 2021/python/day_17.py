#!/usr/bin/python3

from aoc import *

def solve(input_str):
    xmin,xmax,ymin,ymax = ints(input_str)
    count = 0
    max_height = 0
    
    for xv in range(xmax + 1):
        for yv in range(ymin, -ymin + 1):
            height = test(xv, yv, xmin, xmax, ymin, ymax)
            if height != None:
                max_height = max(height, max_height)
                count += 1

    return (max_height, count)

def test(xv, yv, xmin, xmax, ymin, ymax):
    x, y, h = 0, 0, 0

    while x <= xmax and y >= ymin:
        x += xv
        y += yv
        if xv:
            xv -= abs(xv)//xv
        yv -= 1

        h = max(h, y)

        if xmin <= x <= xmax and ymin <= y <= ymax:
            return h


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (25200, 3012)

if __name__ == '__main__':
    main()

