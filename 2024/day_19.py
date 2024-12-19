#!/usr/bin/python3

from aoc import *


def solve(input_str: str):
    towels, patterns = input_str.strip().split("\n\n")
    towels = towels.split(", ")
    patterns = patterns.split("\n")

    T = lambda: defaultdict(T)
    lookup = T()

    def add_towel(towel):
        node = lookup
        for c in towel:
            node = node[c]
        node[""] = True

    for towel in towels:
        add_towel(towel)

    part1, part2 = 0, 0
    for pattern in patterns:
        w = ways_to_make(pattern, lookup)
        part1 += not not w
        part2 += w

    return (part1, part2)


def ways_to_make(pattern, lookup, cache={}):
    if pattern in cache:
        return cache[pattern]

    if pattern == "":
        return 1

    ways = 0
    node = lookup
    for i, c in enumerate(pattern):
        if c not in node:
            break

        node = node[c]
        # valid towel entry
        if "" in node:
            ways += ways_to_make(pattern[i + 1 :], lookup)

    cache[pattern] = ways

    return ways


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (287, 571894474468161)


if __name__ == "__main__":
    main()
