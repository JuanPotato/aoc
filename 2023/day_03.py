#!/usr/bin/python3

from aoc import *

def solve(input_str):
    part1 = 0
    g = [list(l) for l in input_str.split('\n')]
    gears = {c:list() for c in scan_for_gears(g)}
    for val,coords in scan_for_ints(g):
        # check if part number
        if any(any(v not in '.0123456789' for v in get_neighbors(g, c,r)) for c,r in coords):
            part1 += val
        else:
            continue

        neighs = set(n for c,r in coords for n in get_neighbor_coords(g, c, r))
        for n in neighs:
            if n in gears:
                gears[n].append(val)
    
    part2 = sum(v[0]*v[1] for v in gears.values() if len(v) == 2)

    return part1, part2

def scan_for_ints(g):
    coords = []
    val = 0
    for r,row in enumerate(g):
        for c,v in enumerate(row):
            isint = '0' <= v <= '9'
            if isint:
                val = val*10 + int(v)
                coords.append((c, r))

            if coords and (not isint or c == len(row) - 1):
                yield (val,tuple(coords))
                val = 0
                coords = []

def scan_for_gears(g):
    for r,row in enumerate(g):
        for c,v in enumerate(row):
            if v == '*':
                yield (c, r)

def get_neighbors(g, c, r):
    for nc in (c-1,c,c+1):
        for nr in (r-1,r,r+1):
            try:
                yield g[nr][nc]
            except IndexError:
                pass

def get_neighbor_coords(g, c, r):
    for nc in (c-1,c,c+1):
        for nr in (r-1,r,r+1):
            try:
                if g[nr][nc]:
                    pass
                yield (nc, nr)
            except IndexError:
                pass


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (512794, 67779080)

if __name__ == '__main__':
    main()
