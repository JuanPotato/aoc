#!/usr/bin/python3

from aoc import *

def solve(input_str):
    straight = Counter()
    diag = Counter()

    for (ax, ay), _, (bx, by) in parse_list(input_str, eval, str, eval):
        xs = make_range(ax, bx)
        ys = make_range(ay, by)

        if ax == bx or ay == by:
            straight.update((x, y) for y in ys for x in xs)

        else:
            diag.update(zip(xs, ys))

    part1 = sum(1 for v in straight.values() if v >= 2)
    part2 = sum(1 for v in (straight + diag).values() if v >= 2)

    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (6005, 23864)

if __name__ == '__main__':
    main()

