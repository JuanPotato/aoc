#!/usr/bin/python3

from aoc import *


def solve(input_str):
    g = [list(l) for l in input_str.split("\n")]
    send_north(g)
    part1 = get_score(g)

    hashes = []
    scores = []
    dup = False
    while not dup:
        g = cycle(g)
        h = hash("".join(c for r in g for c in r))
        dup = h in hashes
        hashes.append(h)
        scores.append(get_score(g))
    start = hashes.index(h)
    l = len(hashes) - start - 1
    i = (1000000000 - start - 1) % l + start
    part2 = scores[i]

    return part1, part2


def get_score(gg):
    score = 0
    for r, row in enumerate(gg):
        for c in row:
            if c == "O":
                score += len(gg) - r
    return score


def rot90(m):
    return [list(reversed(col)) for col in zip(*m)]


def cycle(gg):
    for _ in range(4):
        send_north(gg)
        gg = rot90(gg)
    return gg


def send_north(gg):
    for c in range(len(gg[0])):
        rocks = 0
        for r in range(len(gg) - 1, 0 - 1, -1):
            match gg[r][c]:
                case "#":
                    for i in range(rocks):
                        gg[r + i + 1][c] = "O"
                    rocks = 0
                case "O":
                    rocks += 1
                    gg[r][c] = "."
        if rocks:
            for i in range(rocks):
                gg[i][c] = "O"


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (109638, 102657)


if __name__ == "__main__":
    main()
