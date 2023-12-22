#!/usr/bin/python3

from aoc import *
from math import *


def solve(input_str):
    pieces = dict()
    bricks = []

    for q, l in enumerate(input_str.split("\n")):
        start, end = list(map(lambda x: tuple(ints(x)), l.split("~")))
        for xyz in iter_xyz(start, end):
            pieces[xyz] = (q, (start, end))
        bricks.append((q, (start, end)))

    def dropshit(bricks, pieces):
        moved = True
        movers = set()
        while moved:
            moved = False
            bricks.sort(key=lambda x: min(x[1][0][2], x[1][1][2]))
            for i in range(len(bricks)):
                q, b = bricks[i]
                minz = min(b[0][2], b[1][2])
                if minz == 0:
                    continue
                drop = 0
                while all(
                    pieces.get((x, y, z - drop - 1), (q, b)) == (q, b)
                    for x, y, z in iter_xyz(*b)
                ):
                    drop += 1
                    if drop == minz:
                        break
                if drop > 0:
                    moved = True
                    movers.add(q)
                    newb = (b[0][0], b[0][1], b[0][2] - drop), (
                        b[1][0],
                        b[1][1],
                        b[1][2] - drop,
                    )
                    for x, y, z in iter_xyz(*b):
                        del pieces[(x, y, z)]
                        pieces[(x, y, z - drop)] = q, newb
                    bricks[i] = q, newb
        return len(movers)

    dropshit(bricks, pieces)

    safes = 0
    dam = 0
    for i, (q, b) in enumerate(bricks):
        safe = True
        # for all pieces of this brick
        for x, y, z in iter_xyz(*b):
            # if there is something directly above it
            if (pp := pieces.get((x, y, z + 1), (q, b))) != (q, b):
                pq, p = pp
                # if there is not a different brick underneath it
                if all(
                    pieces.get((px, py, pz - 1), (q, b)) in ((q, b), (pq, p))
                    for px, py, pz in iter_xyz(*p)
                ):
                    safe = False
                    break

        safes += safe
        if not safe:
            pieces2 = dict(pieces)
            bricks2 = list(bricks)
            bricks2.pop(i)
            for xyz in iter_xyz(*b):
                del pieces2[xyz]
            damage = dropshit(bricks2, pieces2)
            dam += damage

    return safes, dam


def iter_xyz(start, end):
    if start[0] != end[0]:
        _, y, z = start
        for x in make_range(start[0], end[0]):
            yield x, y, z
    elif start[1] != end[1]:
        x, _, z = start
        for y in make_range(start[1], end[1]):
            yield x, y, z
    else:
        x, y, _ = start
        for z in make_range(start[2], end[2]):
            yield x, y, z


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (495, 76158)


if __name__ == "__main__":
    main()
