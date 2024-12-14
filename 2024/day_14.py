#!/usr/bin/python3

from aoc import *


def solve(input_str: str):
    data = chunk(ints(input_str), 4)
    W = 101
    H = 103
    wd = (W - 1) // 2
    hd = (H - 1) // 2
    part1 = 0
    part2 = 0

    for steps in range(10000):
        # pos = defaultdict(int)
        quad = [0, 0, 0, 0]
        for px, py, vx, vy in data:
            px = ((px + vx * steps) % W + W) % W
            py = ((py + vy * steps) % H + H) % H
            # pos[(px, py)] += 1
            if px == wd or py == hd:
                continue
            quad[(px > wd) * 2 + (py > hd)] += 1

        safety = quad[0] * quad[1] * quad[2] * quad[3]

        if steps == 100:
            part1 = safety

        # found through manual checking of min safety a couple times
        if safety < 54233088:
            part2 = steps
            # for y in range(H):
            #     for x in range(W):
            #         print(pos.get((x, y), "."), end="")
            #     print()
            break
    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (230435667, 7709)


if __name__ == "__main__":
    main()
