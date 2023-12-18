#!/usr/bin/python3

from aoc import *


def solve(input_str):
    part1 = get_area(input_str, False)
    part2 = get_area(input_str, True)
    return part1, part2


def get_area(input_str, part2):
    c, r = 0, 0
    holes = []
    edge = 0
    for l in input_str.split("\n"):
        d, n, color = l.split(" ")
        color = color[2:-1]
        n = int(n)
        if part2:
            n = int(color[:-1], 16)
            d = "RDLU"[int(color[-1])]
        edge += n
        match d:
            case "U":
                r -= n
            case "D":
                r += n
            case "R":
                c += n
            case "L":
                c -= n
        holes.append((c, r))

    return int(shoelace(holes) + edge // 2 + 1)


# https://www.theoremoftheday.org/GeometryAndTrigonometry/Shoelace/TotDShoelace.pdf
def shoelace(l):
    A = 0
    for n in range(len(l)):
        A += (l[n - 2][0] * l[n - 1][1]) - (l[n - 1][0] * l[n - 2][1])
    return A / 2


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (56923, 66296566363189)


if __name__ == "__main__":
    main()
