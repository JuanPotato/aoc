#!/usr/bin/python3

from aoc import *

def solve(input_str):
    n = splitint(input_str)
    a = min(n)
    b = max(n)

    costs = partial_sum(range(1, b - a + 1))

    part1 = min(sum(abs(e - i) for e in n) for i in range(a, b + 1))
    part2 = min(sum(costs[abs(e - i)] for e in n) for i in range(a, b+1))

    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (325528, 85015836)

if __name__ == '__main__':
    main()

