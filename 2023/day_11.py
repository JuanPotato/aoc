from aoc import *
from itertools import combinations as comb


def solve(input_str):
    return sumoflengths(input_str, False), sumoflengths(input_str, True)


def sumoflengths(input_str, part2):
    g = [list(l) for l in input_str.split("\n")]
    empty_cols = set(c for c in range(len(g[0])) if all(r[c] == "." for r in g))
    empty_rows = set(r for r, row in enumerate(g) if all(v == "." for v in row))
    points = []
    rr = 0
    for r, row in enumerate(g):
        if r in empty_rows:
            rr += 999999 if part2 else 1
        cc = 0
        for c, v in enumerate(row):
            if c in empty_cols:
                cc += 999999 if part2 else 1
            if v == "#":
                points.append((cc, rr))
            cc += 1
        rr += 1
    return sum(abs(c1 - c2) + abs(r1 - r2) for (c1, r1), (c2, r2) in comb(points, 2))


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (9445168, 742305960572)


if __name__ == "__main__":
    main()
