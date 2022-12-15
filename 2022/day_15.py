#!/usr/bin/python3

from aoc import *

def solve(input_str):
    beacons = []
    for l in lines(input_str):
        sx,sy,bx,by = ints(l)
        d = abs(sx-bx) + abs(sy-by)
        beacons.append((sx,sy,d))


    def find_spaces(ty):
        ranges = []
        for sx,sy,d in beacons:
            if abs(sy-ty) > d:
                continue
            dx = d - abs(sy-ty)
            ranges.append((sx-dx, sx+dx))

        ranges.sort()
        merged_ranges = []
        s,e = None,None
        for ns,ne in ranges:
            if s == None:
                s = ns
                e = ne
                continue
            if e >= ns:
                e = max(e, ne)
            else:
                merged_ranges.append((s,e))
                s = ns
                e = ne
        merged_ranges.append((s, e))

        return merged_ranges

    part1 = sum(e-s for s,e in find_spaces(2000000))

    for ty in range(0, 4000000):
        if len(f := find_spaces(ty)) != 1:
            tx = f[0][1]+1
            part2 = tx * 4000000 + ty
            break

    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (4737443, 11482462818989)

if __name__ == '__main__':
    main()


