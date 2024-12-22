#!/usr/bin/python3

from aoc import *


def solve(input_str: str):
    nums = ints(input_str)
    part1 = 0
    cc = Counter()
    for n in nums:
        done = set()
        a, b, c, d = None, None, None, None
        p = n % 10
        for _ in range(2000):
            n = (n ^ (n << 6)) & 0xFFFFFF
            n = (n ^ (n >> 5)) & 0xFFFFFF
            n = (n ^ (n << 11)) & 0xFFFFFF
            p2 = n % 10
            a, b, c, d = b, c, d, p2 - p
            p = p2
            key = (a, b, c, d)
            if None in key:
                continue
            if key in done:
                continue
            done.add(key)
            cc[key] += p2

        part1 += n
    part2 = cc.most_common(1)[0][1]

    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (19877757850, 2399)


if __name__ == "__main__":
    main()
