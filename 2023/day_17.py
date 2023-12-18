#!/usr/bin/python3

from aoc import *
import heapq


def solve(input_str):
    part1 = get_min_loss(input_str, (1, 4))
    part2 = get_min_loss(input_str, (4, 11))
    return part1, part2


def get_min_loss(input_str, step_range=(1, 4)):
    g = [list(map(int, l)) for l in input_str.split("\n")]
    gc, gr = len(g[0]) - 1, len(g) - 1
    paths = [(0, (0, 0), "")]
    mins = {}
    dest = {
        "U": [(0, i * -1) for i in range(*step_range)],
        "D": [(0, i * 1) for i in range(*step_range)],
        "L": [(i * -1, 0) for i in range(*step_range)],
        "R": [(i * 1, 0) for i in range(*step_range)],
    }
    DD = {"U": "UD", "D": "UD", "L": "LR", "R": "LR", "": ""}
    NND = {"U": "LR", "D": "LR", "L": "UD", "R": "UD", "": "DR"}

    while paths:
        loss, (c, r), d = heapq.heappop(paths)
        if (c, r) == (gc, gr):
            return loss
        ddd = DD[d]
        if (c, r, ddd) in mins and mins[(c, r, ddd)] <= loss:
            continue
        else:
            mins[(c, r, ddd)] = loss

        for nd in NND[d]:
            for dc, dr in dest[nd]:
                bail = False
                nc = c + dc
                nr = r + dr
                if not (0 <= nc <= gc and 0 <= nr <= gr):
                    continue

                nloss = loss
                for rr in make_range(r, nr):
                    for cc in make_range(c, nc):
                        if (cc, rr) == (c, r):
                            continue
                        nloss += g[rr][cc]

                heapq.heappush(paths, (nloss, (nc, nr), nd))
    return None


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (970, 1149)


if __name__ == "__main__":
    main()
