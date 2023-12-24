#!/usr/bin/python3

from aoc import *
from math import *
import z3
import itertools


def solve(input_str):
    bmin, bmax = 200000000000000, 400000000000000
    mb = []
    eqs = []
    x, y, z, j, k, l = z3.Ints("x y z j k l")
    for i, line in enumerate(input_str.split("\n")):
        pos, vel = tuple(map(eval, line.split(" @ ")))
        x0, y0, z0 = pos
        vx, vy, vz = vel
        x1, y1, z1 = x0 + vx, y0 + vy, z0 + vz
        m = (y1 - y0) / (x1 - x0)
        b = y0 - m * x0
        mb.append(((m, b), pos, vel))
        t = z3.Int(f"t_{i}")
        eqs.append(x0 + vx * t == x + j * t)
        eqs.append(y0 + vy * t == y + k * t)
        eqs.append(z0 + vz * t == z + l * t)

    s = z3.Solver()
    s.add(*eqs)
    s.check()
    res = s.model()
    part2 = res[x].as_long() + res[y].as_long() + res[z].as_long()

    part1 = 0
    for ((m0, b0), pos0, vel0), ((m1, b1), pos1, vel1) in itertools.combinations(mb, 2):
        x0, y0, z0 = pos0
        x1, y1, z1 = pos1
        vx0, vy0, vz0 = vel0
        vx1, vy1, vz1 = vel1
        if m0 == m1:
            x, y = None, None
            future = None
        else:
            x = (b1 - b0) / (m0 - m1)
            y = m0 * x + b0
            future = (x > x0) == (vx0 > 0) and (x > x1) == (vx1 > 0)

        if future and bmin <= x <= bmax and bmin <= y <= bmax:
            part1 += 1

    return part1, part2


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (16939, 931193307668256)


if __name__ == "__main__":
    main()
