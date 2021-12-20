#!/usr/bin/python3

from aoc import *
import time

def solve(input_str):
    report = parse(input_str.strip())
    scanners, beacons = merge(report)
    largest_distance = max(sum(abs(a-b) for a,b in zip(p1,p2)) for p1 in scanners for p2 in scanners)
    return (len(beacons), largest_distance)

def parse(inp):
    sc = inp.split('\n\n')
    sc = [lmap(eval, l.split('\n')[1:]) for l in sc]
    return sc

def merge(reports):
    big = set(reports.pop(0))
    scanners = [(0,0)]
    while reports:
        to_merge = []

        for i, guess in enumerate(reports):
            score, points, scanner = match(big, guess)
            if score >= 12:
                to_merge.append((i, points, scanner))

        for i, points, scanner in to_merge[::-1]:
            reports.pop(i)
            scanners.append(scanner)
            big.update(set(points))

    return scanners, big

transforms = [
    lambda x,y,z: ( z,  y, -x), lambda x,y,z: (-y,  z, -x), lambda x,y,z: (-z, -y, -x),
    lambda x,y,z: ( y, -z, -x), lambda x,y,z: ( z,  x,  y), lambda x,y,z: (-x,  z,  y),
    lambda x,y,z: (-z, -x,  y), lambda x,y,z: ( x, -z,  y), lambda x,y,z: ( y,  x, -z),
    lambda x,y,z: (-x,  y, -z), lambda x,y,z: (-y, -x, -z), lambda x,y,z: ( x, -y, -z),
    lambda x,y,z: ( y,  z,  x), lambda x,y,z: (-z,  y,  x), lambda x,y,z: (-y, -z,  x),
    lambda x,y,z: ( z, -y,  x), lambda x,y,z: ( x,  z, -y), lambda x,y,z: (-z,  x, -y),
    lambda x,y,z: (-x, -z, -y), lambda x,y,z: ( z, -x, -y), lambda x,y,z: ( x,  y,  z),
    lambda x,y,z: (-y,  x,  z), lambda x,y,z: (-x, -y,  z), lambda x,y,z: ( y, -x,  z),
]


def dist(a,b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def match(reference, points):
    score = 0
    best = points
    best_o = (0,0,0)

    for t in transforms:
        moved = [t(*p) for p in points]

        m = (0, None)
        dists = {}
        for a in reference:
            for b in moved:
                d = dist(a, b)
                dists[d] = (dd := (dists.get(d, 0) + 1))
                if dd > m[0]:
                    m = (dd, d)

        s, offset = m

        if s > score:
            score = s
            best = moved
            best_o = offset

        if s >= 12:
            break

    xo,yo,zo = best_o
    return score, [(x+xo,y+yo,z+zo) for x,y,z in best], best_o

def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (372, 12241)

if __name__ == '__main__':
    main()

