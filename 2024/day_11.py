#!/usr/bin/python3

from aoc import *


def solve(input_str: str):
    stones = Counter(ints(input_str))
    part1 = sum(n_step(stones, 25).values())
    part2 = sum(n_step(stones, 75).values())
    return part1, part2


# caching not necessary but cool
def step(n, cache={}):
    if n == 0:
        return (1,)

    if n not in cache:
        if len(sn := str(n)) % 2 == 0:
            cache[n] = (int(sn[: len(sn) // 2]), int(sn[len(sn) // 2 :]))
        else:
            cache[n] = (2024 * n,)

    return cache[n]


def all_step(stones):
    new_stones = Counter()
    for stone, count in stones.items():
        for ns in step(stone):
            new_stones[ns] += count
    return new_stones


def n_step(stones, n):
    for i in range(n):
        stones = all_step(stones)
    return stones


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (194782, 233007586663131)


if __name__ == "__main__":
    main()
