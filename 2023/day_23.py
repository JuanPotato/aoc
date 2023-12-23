#!/usr/bin/python3

from aoc import *
from math import *


def solve(input_str):
    return (
        find_the_longest_path_please(input_str),
        find_the_longest_path_please(input_str, True),
    )


def find_the_longest_path_please(input_str, part2=False):
    g = [list(l) for l in input_str.split("\n")]
    sr = 0
    sc = g[0].index(".")
    gr = len(g) - 1
    gc = g[gr].index(".")
    paths = [(0, {(sc, sr)}, (sc, sr))]
    mm = 0

    nodes = [(sc, sr), (gc, gr)]

    def get_moves(c, r, ps, p2=part2):
        for nc, nr in ((c - 1, r), (c + 1, r), (c, r - 1), (c, r + 1)):
            if nc < 0 or nr < 0 or nr >= len(g) or nc >= len(g[0]):
                continue
            if (nc, nr) in ps:
                continue
            if g[nr][nc] == "#":
                continue
            if not p2:
                match g[nr][nc], nc - c, nr - r:
                    case ">", -1, _:
                        continue
                    case "<", 1, _:
                        continue
                    case "^", _, 1:
                        continue
                    case "v", _, -1:
                        continue
            yield nc, nr

    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == "#":
                continue
            if len(list(get_moves(c, r, tuple(), True))) > 2:
                nodes.append((c, r))

    paths = defaultdict(dict)
    for c, r in nodes:
        moves = list(get_moves(c, r, tuple()))
        for mc, mr in moves:
            l = 1
            ps = {(c, r), (mc, mr)}
            moves = list(get_moves(mc, mr, ps))
            while len(moves) == 1:
                l += 1
                mc, mr = moves[0]
                ps.add((mc, mr))
                moves = list(get_moves(mc, mr, ps))
            paths[(c, r)][(mc, mr)] = l
    snake = [[(sc, sr)]]
    while snake:
        s = snake.pop()
        for opt in paths[s[-1]]:
            if opt in s:
                continue
            snake.append(s + [opt])
        if s[-1] == (gc, gr):
            mmm = sum(paths[a][b] for a, b in window(s, 2))
            if mmm > mm:
                mm = mmm
    return mm


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (2030, 6390)


if __name__ == "__main__":
    main()
