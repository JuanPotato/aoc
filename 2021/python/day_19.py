#!/usr/bin/python3

from aoc import *

def solve(input_str):
    report = parse(input_str.strip())
    scanners, beacons = merge(report)
    largest_distance = max(sum(abs(a-b) for a,b in zip(p1,p2)) for p1 in scanners for p2 in scanners)
    return (len(beacons), largest_distance)

def parse(inp):
    sc = inp.split('\n\n')
    sc = [lmap(eval, l.split('\n')[1:]) for l in sc]
    return sc

def merge(ss):
    big = set(ss.pop(0))
    scanners = [(0,0)]
    while ss:
        best_i = 0
        best, score = None, 0.0
        for i,guess in enumerate(ss):
            newscore, newpoints, scanner = match(big, guess)

            if newscore > score:
                best_i = i
                score = newscore
                best = newpoints
                best_scanner = scanner

            if score >= 12:
                # good enough
                break

        if score < 12:
            raise Exception("Unimplemented")

        ss.pop(best_i)
        scanners.append(best_scanner)
        big = big.union(set(best))

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

def match(pointsa, pointsb):
    score = 0
    best = pointsb
    best_o = (0,0,0)


    for t in transforms:
        moved = [t(*p) for p in pointsb]
        c = Counter(tuple(aa-bb for aa,bb in zip(a,b)) for a in pointsa for b in moved)
        offset, s = c.most_common()[0]

        if s > score:
            score = s
            best = moved
            best_o = offset

    xo,yo,zo = best_o
    return score, [(x+xo,y+yo,z+zo) for x,y,z in best], best_o

def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (372, 12241)

if __name__ == '__main__':
    main()

