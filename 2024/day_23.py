#!/usr/bin/python3

from aoc import *
import itertools


def solve(input_str: str):
    connections = chunk(words(input_str), 2)
    comps = defaultdict(set)
    for a, b in connections:
        comps[a].add(b)
        comps[b].add(a)
    for a in comps:
        comps[a].add(a)

    part1 = 0
    max_d = set()

    for a, b, c in itertools.combinations(comps, 3):
        if a in comps[b] and b in comps[c] and c in comps[a]:
            if a[0] == "t" or b[0] == "t" or c[0] == "t":
                part1 += 1

    for a, b in itertools.combinations(comps, 2):
        if d := comps[a] & comps[b]:
            for k in d:
                d = d & comps[k]
            if len(d) > len(max_d):
                max_d = d

    part2 = ",".join(sorted(max_d))

    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1352, "dm,do,fr,gf,gh,gy,iq,jb,kt,on,rg,xf,ze")


if __name__ == "__main__":
    main()
