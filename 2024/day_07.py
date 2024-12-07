#!/usr/bin/python3

from aoc import *
import itertools


def solve(input_str: str):
    grid = parse_grid(input_str, int, sep="[: ]+")
    # this produces marginal time savings :)
    miss = []
    part1 = 0
    for row in grid:
        res = do(row)
        if res:
            part1 += res
        else:
            miss.append(row)
    part2 = part1 + sum(map(lambda x: do(x, True), miss))
    return part1, part2


def do(values, part2=False):
    test, *rest = values
    for ops in itertools.product("+*|" if part2 else "+*", repeat=len(rest) - 1):
        cur = rest[0]
        for i, op in enumerate(ops):
            if op == "+":
                cur += rest[i + 1]
            elif op == "*":
                cur *= rest[i + 1]
            elif op == "|":
                cur = int(f"{cur}{rest[i+1]}")

        if cur == test:
            return cur
    return 0


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (14711933466277, 286580387663654)


if __name__ == "__main__":
    main()
