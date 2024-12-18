#!/usr/bin/python3

from aoc import *


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


def do(row, part2=False):
    target, n1, *nums = row
    return do_inner(target, n1, nums, part2)


def do_inner(target, cur, nums, part2=False):
    if cur > target:
        return 0

    if not nums:
        if cur == target:
            return target
        return 0

    n, *nums = nums
    if res := do_inner(target, cur + n, nums, part2):
        return res
    if res := do_inner(target, cur * n, nums, part2):
        return res
    if part2 and (res := do_inner(target, int(f"{cur}{n}"), nums, part2)):
        return res
    return 0


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (14711933466277, 286580387663654)


if __name__ == "__main__":
    main()
