#!/usr/bin/python3

from aoc import *
from typing import NamedTuple
import time

def solve(input_str):
    all_cubes = []
    init_cubes = []

    for l in input_str.strip().split('\n'):
        on = l[1] == 'n'
        xmin, xmax, ymin, ymax, zmin, zmax = ints(l)
        cube = Cube(Range(xmin, xmax), Range(ymin, ymax), Range(zmin, zmax))

        new_all_cubes = []
        for other in all_cubes:
            if other.intersects(cube):
                new_all_cubes.extend(other - cube)
            else:
                new_all_cubes.append(other)

        if on:
            new_all_cubes.append(cube)

        all_cubes = new_all_cubes

        
        xmin, ymin, zmin = [max(-50, e) for e in (xmin, ymin, zmin)]
        xmax, ymax, zmax = [min(e, 50) for e in (xmax, ymax, zmax)]
        init_cube = Cube(Range(xmin, xmax), Range(ymin, ymax), Range(zmin, zmax))
        if init_cube.unwrap() == None:
            continue

        new_init_cubes = []
        for other in init_cubes:
            if other.intersects(init_cube):
                new_init_cubes.extend(other - init_cube)
            else:
                new_init_cubes.append(other)

        if on:
            new_init_cubes.append(init_cube)

        init_cubes = new_init_cubes

    part1 = sum(map(Cube.volume, init_cubes))
    part2 = sum(map(Cube.volume, all_cubes))

    return (part1, part2)


class Range(NamedTuple):
    min: int
    max: int

    def size(self):
        return self.max - self.min + 1

    def intersects(self, other):
        if self.min <= other.min <= self.max or self.min <= other.max <= self.max:
            return True
        if other.min <= self.min <= other.max or other.min <= self.max <= other.max:
            return True
        return False

    def segment(self, other):
        result = []
        antiresult = []

        # S O S O
        if self.min <= other.min <= self.max <= other.max:
            result.append(Range(self.min, other.min - 1))
            antiresult.append(Range(other.min, self.max))

        # O S O S
        elif other.min <= self.min <= other.max <= self.max:
            antiresult.append(Range(self.min, other.max))
            result.append(Range(other.max + 1, self.max))

        # S O O S
        elif self.min <= other.min <= other.max <= self.max:
            result.append(Range(self.min, other.min - 1))
            antiresult.append(Range(other.min, other.max))
            result.append(Range(other.max + 1, self.max))

        # O S S O
        elif other.min <= self.min <= self.max <= other.max:
            antiresult.append(Range(self.min, self.max))

        else:
            result.append(self)

        return (
            [r for r in map(Range.unwrap, result) if r],
            [a for a in map(Range.unwrap, antiresult) if a]
        )

    def unwrap(self):
        if self.max < self.min:
            return None
        else:
            return self


class Cube(NamedTuple):
    x: Range
    y: Range
    z: Range

    def volume(self):
        return self.x.size() * self.y.size() * self.z.size()

    def intersects(self, other):
        return self.x.intersects(other.x) and self.y.intersects(other.y) and self.z.intersects(other.z)
    
    def subtract(self, other):
        xs, (antix,) = self.x.segment(other.x)
        ys, (antiy,) = self.y.segment(other.y)
        zs, (antiz,) = self.z.segment(other.z)
        result = []

        for x in (*xs, antix):
            for y in (*ys, antiy):
                for z in (*zs, antiz):
                    if (x,y,z) == (antix,antiy,antiz): continue
                    result.append(Cube(x,y,z))

        return [r for r in map(Cube.unwrap, result) if r]

    def unwrap(self):
        if not self.x.unwrap() or not self.y.unwrap() or not self.z.unwrap():
            return None
        else:
            return self

    def __sub__(self, other):
        return self.subtract(other)



def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (524792, 1213461324555691)

if __name__ == '__main__':
    main()

