#!/usr/bin/python3

from aoc import *
import z3


def solve(input_str: str):
    nums = ints(input_str)
    part1 = 0
    part2 = 0

    for ax, ay, bx, by, px, py in chunk(nums, 6):
        min_cost = None
        for a in range(100):
            rx = px - a * ax
            ry = py - a * ay
            if rx < 0 or ry < 0:
                continue
            if rx % bx != 0 or ry % by != 0 or (ry // by) != (rx // bx):
                continue
            cost = a * 3 + rx // bx
            if min_cost == None or cost < min_cost:
                min_cost = cost
        part1 += min_cost or 0

    s = z3.Solver()
    a2, b2 = z3.Ints(f"a2 b2")
    for ax, ay, bx, by, px, py in chunk(nums, 6):
        s.push()
        s.add(ax * a2 + bx * b2 == (10000000000000 + px))
        s.add(ay * a2 + by * b2 == (10000000000000 + py))
        if s.check() == z3.sat:
            res = s.model()
            part2 += res[a2].as_long() * 3 + res[b2].as_long()
        s.pop()

    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (39996, 73267584326867)


if __name__ == "__main__":
    main()
