#!/usr/bin/python3

from aoc import *

def solve(input_str):
    part1 = plot_cubes(input_str)
    part2 = plot_cubes_good(input_str)

    return (part1, part2)


def plot_cubes(input_str):
    cubes = [tuple(ints(l)) for l in lines(input_str)]
    X = max(x for x,y,z in cubes) + 1
    Y = max(y for x,y,z in cubes) + 1
    Z = max(z for x,y,z in cubes) + 1
    xy_plane = [[[0 for _ in range(X+1)] for _ in range(Y+1)] for _ in range(Z+1)]
    xz_plane = [[[0 for _ in range(X+1)] for _ in range(Y+1)] for _ in range(Z+1)]
    yz_plane = [[[0 for _ in range(X+1)] for _ in range(Y+1)] for _ in range(Z+1)]
    planes = [xy_plane, xz_plane, yz_plane]
    for x,y,z in cubes:
        xy_plane[z][y][x] += 1
        xy_plane[z+1][y][x] += 1
        xz_plane[z][y][x] += 1
        xz_plane[z][y+1][x] += 1
        yz_plane[z][y][x] += 1
        yz_plane[z][y][x+1] += 1
    return sum(d for p in planes for s in p for r in s for d in r if d == 1)

def plot_cubes_good(input_str):
    cubes = [tuple(ints(l)) for l in lines(input_str)]
    X = max(x for x,y,z in cubes) + 2
    Y = max(y for x,y,z in cubes) + 2
    Z = max(z for x,y,z in cubes) + 2

    AIR = 0
    LAVA = 1
    WATER = 2
    
    lava = [[[AIR for _ in range(X)] for _ in range(Y)] for _ in range(Z)]
    for x,y,z in cubes:
        lava[z][y][x] = LAVA

    flooding = {(0,0,0)}
    while flooding:
        x,y,z = flooding.pop()
        if lava[z][y][x] != AIR:
            continue

        lava[z][y][x] = WATER

        neigh = (
            (x-1, y, z),
            (x+1, y, z),
            (x, y-1, z),
            (x, y+1, z),
            (x, y, z-1),
            (x, y, z+1),
        )
        for nx,ny,nz in neigh:
            if not (0<=nx<X and 0<=ny<Y and 0<=nz<Z):
                continue
            if lava[nz][ny][nx] == AIR:
                flooding.add((nx, ny, nz))

    xy_plane = [[[0 for _ in range(X+1)] for _ in range(Y+1)] for _ in range(Z+1)]
    xz_plane = [[[0 for _ in range(X+1)] for _ in range(Y+1)] for _ in range(Z+1)]
    yz_plane = [[[0 for _ in range(X+1)] for _ in range(Y+1)] for _ in range(Z+1)]
    planes = [xy_plane, xz_plane, yz_plane]
    for x,y,z in cubes:
        if lava[z-1][y][x] == WATER:
            xy_plane[z][y][x] += 1
        if lava[z+1][y][x] == WATER:
            xy_plane[z+1][y][x] += 1

        if lava[z][y-1][x] == WATER:
            xz_plane[z][y][x] += 1
        if lava[z][y+1][x] == WATER:
            xz_plane[z][y+1][x] += 1

        if lava[z][y][x-1] == WATER:
            yz_plane[z][y][x] += 1
        if lava[z][y][x+1] == WATER:
            yz_plane[z][y][x+1] += 1

    return sum(d for p in planes for s in p for r in s for d in r if d == 1)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (4444, 2530)

if __name__ == '__main__':
    main()


