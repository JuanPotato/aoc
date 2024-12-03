#!/usr/bin/python3

from aoc import *


def solve(input_str):
    do = True
    part1 = 0
    part2 = 0
    for j, k, dont in re.findall(
        r"mul\((\d{1,3}),(\d{1,3})\)|(do|don\'t)\(\)", input_str
    ):
        match dont:
            case "do":
                do = True
            case "don't":
                do = False
            case "":
                part1 += int(j) * int(k)
                part2 += int(j) * int(k) * do

    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (187825547, 85508223)


if __name__ == "__main__":
    main()
