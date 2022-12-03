#!/usr/bin/python3

from aoc import *

def solve(input_str):
    data = list(sum(map(int, d.split("\n"))) for d in input_str.strip().split("\n\n"))
    data.sort()

    part1 = max(data)
    part2 = sum(data[-3:])

    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (72240, 210957)

if __name__ == '__main__':
    main()


