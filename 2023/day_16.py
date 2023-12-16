#!/usr/bin/python3

from aoc import *


def solve(input_str):
    g = [list(l) for l in input_str.split("\n")]
    return part1(g), part2(g)


def part2(g):
    W = len(g[0])
    H = len(g)
    starts = []
    starts += [(c, -1, "D") for c in range(W)]
    starts += [(c, H, "U") for c in range(W)]
    starts += [(-1, r, "R") for r in range(H)]
    starts += [(W, r, "L") for r in range(H)]
    return max(part1(g, s) for s in starts)


def part1(g, start=(-1, 0, "R")):
    e = [[False for _ in range(len(r))] for r in g]
    light = [start]
    done = set(light)

    def add(c, r, d):
        if (c, r, d) not in done:
            done.add((c, r, d))
            light.append((c, r, d))

    while light:
        lc, lr, d = light.pop(0)
        live = True

        while live:
            match d:
                case "R":
                    lc += 1
                case "L":
                    lc -= 1
                case "U":
                    lr -= 1
                case "D":
                    lr += 1

            if lc < 0 or lr < 0 or lr >= len(g) or lc >= len(g[0]):
                break
            e[lr][lc] = True

            match g[lr][lc]:
                case "/":
                    d = {"L": "D", "R": "U", "D": "L", "U": "R"}[d]
                case "\\":
                    d = {"L": "U", "R": "D", "D": "R", "U": "L"}[d]
                case "|":
                    if d in ("L", "R"):
                        add(lc, lr, "U")
                        add(lc, lr, "D")
                        live = False
                case "-":
                    if d in ("U", "D"):
                        add(lc, lr, "L")
                        add(lc, lr, "R")
                        live = False
    return sum(c for r in e for c in r)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (7236, 7521)


if __name__ == "__main__":
    main()
